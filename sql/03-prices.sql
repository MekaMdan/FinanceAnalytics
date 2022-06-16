CREATE TABLE IF NOT EXISTS prices (
    ticker_id INT REFERENCES tickers(id),
    price MONEY,
    price_date DATE NOT NULL, 
    PRIMARY KEY(price_date, ticker_id)
);