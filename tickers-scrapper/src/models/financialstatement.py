import datetime as dt

class FinancialStatement:
    ticker_id: int
    statement_date: dt.date
    stocks_amount: int
    div_yield: float
    assets: int
    disponibility: int
    current_assets: int
    gross_debt: int
    net_debt: int
    liquid_equity: int
    net_revenue: int
    ebit: int
    liquid_profit: int

    def __init__(self,ticker_id: int, statement_date: dt.date,
        stocks_amount: int, div_yield: float,assets: int, disponibility: int,
        current_assets: int, gross_debt: int, net_debt: int,liquid_equity: int,
        net_revenue: int, ebit: int, liquid_profit: int):

        self.ticker_id = ticker_id
        self.statement_date = statement_date
        self.stocks_amount = stocks_amount
        self.div_yield = div_yield
        self.assets = assets
        self.disponibility = disponibility
        self.current_assets = current_assets
        self.gross_debt = gross_debt
        self.net_debt = net_debt
        self.liquid_equity = liquid_equity
        self.net_revenue = net_revenue
        self.ebit = ebit
        self.liquid_profit = liquid_profit
