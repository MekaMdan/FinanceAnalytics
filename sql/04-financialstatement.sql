CREATE TABLE IF NOT EXISTS financialstatements (
    id INT PRIMARY KEY generated always as identity,
    ticker_id INT REFERENCES tickers(id),
    statement_date DATE NOT NULL,
    stocks_amount BIGINT NOT NULL,
    div_yield NUMERIC(5,2) NOT NULL,
    assets BIGINT NOT NULL,
    disponibility BIGINT NOT NULL,
    current_assets BIGINT NOT NULL,
    gross_debt BIGINT NOT NULL,
    net_debt BIGINT NOT NULL,
    liquid_equity BIGINT NOT NULL,
    net_revenue BIGINT NOT NULL,
    ebit BIGINT NOT NULL,
    liquid_profit BIGINT NOT NULL
);