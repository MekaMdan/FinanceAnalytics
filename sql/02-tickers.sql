CREATE TABLE IF NOT EXISTS tickers (
    id INT PRIMARY KEY generated always as identity,
    ticker_code VARCHAR(5),
    enterprise_name VARCHAR(32),
    sector_id INT,
    CONSTRAINT fk_sector FOREIGN KEY(sector_id) REFERENCES sectors(id)
);