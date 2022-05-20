CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE IF NOT EXISTS tickers (
    id INT PRIMARY KEY generated always as identity,
    ticker VARCHAR(5),
    enterprise_name VARCHAR(32)
);