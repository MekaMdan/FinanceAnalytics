from ..models.scrapper_interface import ScrapperInterface
from ..models.financialstatement import FinancialStatement
from ..models.price import Price
from typing import Tuple, Dict, List, Callable
from requests import get
from bs4 import BeautifulSoup, ResultSet
import datetime as dt

class FundamentusScrapper(ScrapperInterface):
    def __init__(self) -> None:
        self.parsing_routines: List[Callable] = [
            self._parse_price,
            self._parse_metadata,
            self._parse_div_yield,
            self._parse_assets,
            self._parse_results
        ]
        self.price : Price = None
        self.financialstatement : FinancialStatement = None

    def scrap(self, message: Dict) -> Tuple[Price, FinancialStatement]:
        ticker_name = message['ticker_name']
        self.price : Price = Price()
        self.financialstatement : FinancialStatement = FinancialStatement()
        self.price.ticker_code = ticker_name
        self.financialstatement.ticker_code = ticker_name

        url = "https://www.fundamentus.com.br/detalhes.php?papel="
        target_url = url + ticker_name
        agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/\
537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

        try:
            page = get(target_url, headers=agent)
            soup = BeautifulSoup(page.text, 'html.parser')

            tables = soup.find_all('table', attrs={"w728"})
            for (table, parser) in zip(tables, self.parsing_routines):
                parser(table)

        except Exception as e:
            print("Erro %s ao ler a pagina", str(e))
            raise Exception("paper indisponivel")

        return (self.price, self.financialstatement)

    def _parse_price(self, table: ResultSet):
        # get cotação
        price_finder = table.find('td', attrs={"class":"data destaque w3"})
        price_value = price_finder.find('span').getText().replace(',','.')
        self.price.price_value = float(price_value)
        
        # get cotação data
        next_finder = price_finder.find_next('td', attrs={"class":"data"})
        data_price_finder = next_finder.find_next('td', attrs={"class":"data"})
        price_data = data_price_finder.find('span').getText()
        p_date = dt.datetime.strptime(price_data, '%d/%m/%Y').date()
        self.price.price_date = p_date

    def _parse_metadata(self, table: ResultSet):
        # get data balanço util
        price_data_find = table.find('td', attrs={"class":"data w2"})
        price_data = price_data_find.find('span').getText()
        s_data = dt.datetime.strptime(price_data, '%d/%m/%Y').date()
        self.financialstatement.statement_date = s_data

        # get nmro de ações 
        b4_nmo_finder = price_data_find.find_next('td', attrs={"class":"data"})
        nmo_finder = b4_nmo_finder.find_next('td', attrs={"class":"data"})
        nmo = nmo_finder.find('span').getText().replace('.','')
        self.financialstatement.stocks_amount = int(nmo)

    def _parse_div_yield(self, table: ResultSet):
        # get div yield
        div_yield_ant = table.find('span', attrs={"title":"Dividend Yield: Dividendo pago por ação dividido pelo preço da ação. É o rendimento gerado para o dono da ação pelo pagamento de dividendos."})
        div_yield_span = div_yield_ant.find_next('span')
        div_yield = div_yield_span.find_next('span').getText().replace('%','').replace(',','.')
        self.financialstatement.div_yield = float(div_yield)

    def _parse_assets(self, table: ResultSet):
        # get ativos
        atv_ant = table.find('span', attrs={"title":"Todos os bens, direitos e valores a receber de uma entidade"})
        atv_span = atv_ant.find_next('span')
        atv = atv_span.find_next('span').getText().replace('.','')
        self.financialstatement.assets = int(atv)

        # get debt
        ant = table.find('span', attrs={"title":"Dívida Bruta é obtida somando-se as dívidas de curto e longo prazo mais as debêntures de curto e longo prazo."})
        span = ant.find_next('span')
        debt = span.find_next('span').getText().replace('.','')
        self.financialstatement.gross_debt = int(debt)

        # get disponibilidade
        disp_ant = table.find('span', attrs={"title":"Contas que representam bens numerários (Dinheiro)"})
        disp_span = disp_ant.find_next('span')
        disp = disp_span.find_next('span').getText().replace('.','')
        self.financialstatement.disponibility = int(disp)

        # get liq debt
        ant = table.find('span', attrs={"title":"Dívida Bruta menos Disponibilidades. Se este valor é negativo, significa que a empresa possui caixa líquido positivo."})
        span = ant.find_next('span')
        liq_debt = span.find_next('span').getText().replace('.','')
        self.financialstatement.net_debt = int(liq_debt)

        # get ativo circulante
        atv_circ_ant = table.find('span',attrs={"title":"Bens ou direitos que podem ser convertido em dinheiro em curto prazo"})
        atv_circ_span = atv_circ_ant.find_next('span')
        atv_circ = atv_circ_span.find_next('span').getText().replace('.','')
        self.financialstatement.current_assets = int(atv_circ)

        # get liq net
        ant = table.find('span', attrs={"title":"O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, a diferença entre o valor dos ativos e dos passivos e resultado de exercícios futuros representa o PL (Patrimônio Líquido), que é o valor contábil devido pela pessoa jurídica aos sócios ou acionistas."})
        span = ant.find_next('span')
        liq_net = span.find_next('span').getText().replace('.','')
        self.financialstatement.net_revenue = int(liq_net)

    def _parse_results(self, table: ResultSet):
        # get receita liquida
        anterior = table.find('span', attrs={"title":"Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos."})
        span = anterior.find_next('span')
        rec_liq = span.find_next('span').getText().replace('.','')
        self.financialstatement.liquid_equity = int(rec_liq)

        # get ebit
        anterior = table.find('span', attrs={"title":"Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas"})
        span = anterior.find_next('span')
        ebit = span.find_next('span').getText().replace('.','')
        self.financialstatement.ebit = int(ebit)

        # get lucro liquido
        anterior = table.find('span', attrs={"title":"O que sobra das vendas após a dedução de todas as despesas"})
        span = anterior.find_next('span')
        lcr_lqd = span.find_next('span').getText().replace('.','')
        self.financialstatement.liquid_profit = int(lcr_lqd)
