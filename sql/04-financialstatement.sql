CREATE TABLE IF NOT EXISTS financialstatements (
    id INT PRIMARY KEY generated always as identity,
    ticker_id INT REFERENCES tickers(id) NOT NULL,
    statement_date DATE,
    stocks_amount INT NOT NULL,
    div_yield NUMERIC(5,2),
    assets BIGINT,
    disponibility BIGINT,
    current_assets BIGINT,
    gross_debt BIGINT,
    net_debt BIGINT,
    liquid_equity BIGINT,
    net_revenue BIGINT,
    ebit BIGINT,
    liquid_profit BIGINT
);