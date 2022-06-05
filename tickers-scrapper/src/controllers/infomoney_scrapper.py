from ..models.scrapper_interface import ScrapperInterface
from typing import List
from ..models.ticker import Ticker
from requests import get
from bs4 import BeautifulSoup, ResultSet

class InfomoneyScrapper(ScrapperInterface):
    def scrap(self) -> List[Ticker]:
        target_url='https://www.infomoney.com.br/cotacoes/empresas-b3/'
        try:
            page = get(target_url)

            soup = BeautifulSoup(page.text, 'html.parser')
            infos = soup.find_all('table', attrs={"class":"default-table"})
            sector_id = 1
            tickers_list = list()

            for table in infos:
                tickers_list += self._scrap_enterprises(sector_id, table)
                sector_id +=1
            
            return tickers_list

        except Exception as e:
            print(f"Erro {e} ao ler a pagina")

    def _is_ordinary(self, ticker_code:str) -> bool:
        if (ticker_code[-1:]!= '3'):
            return False
        if (len(ticker_code)!=5):
            return False
        return True

    def _scrap_enterprises(self, sector_id: int, table: ResultSet):
        tickers_list = list()
        for row in table.find_all('tr'):
            enterpriseName = row.find('td', attrs={"class":"higher"})
            if (enterpriseName != None):
                tickers = row.find_all('a')
                tickers_list += self._scrap_tickers(
                    sector_id, 
                    tickers, 
                    enterpriseName.getText() 
                )
        return tickers_list
                
                

    def _scrap_tickers(self, sector_id: int, tickers: ResultSet, 
    enterprise_name: str)-> List[Ticker]:
        tickers_list = list()
        for entry in tickers:
            cod = entry.getText()
            if(self._is_ordinary(cod)):
                tickers_list.append(Ticker(cod, enterprise_name, sector_id))
        return tickers_list