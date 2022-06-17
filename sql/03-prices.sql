CREATE TABLE IF NOT EXISTS prices (
    id INT PRIMARY KEY generated always as identity,
    ticker_id INT REFERENCES tickers(id),
    price MONEY,
    price_date DATE NOT NULL
);