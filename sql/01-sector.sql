CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE IF NOT EXISTS sectors (
    id INT PRIMARY KEY generated always as identity,
    sector_name VARCHAR(40)
);

INSERT INTO 
    sectors (sector_name) 
VALUES 
    ('Bens Industriais'), 
    ('Consumo Cíclico'),
    ('Consumo não Cíclico'), 
    ('Financeiro'), 
    ('Materiais Básicos'),
    ('Outros'),
    ('Petróleo, Gás e Biocombustíveis'),
    ('Saúde'),
    ('Tecnologia da Informação'),
    ('Telecomunicações'),
    ('Utilidade Pública')
