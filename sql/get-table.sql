SELECT  ticker_code, sector_name,statement_date, stocks_amount, div_yield, assets, disponibility, current_assets, gross_debt, net_debt, liquid_equity, net_revenue, ebit, liquid_profit, prices.price_date, prices.price_value
FROM public.financialstatements
inner join public.tickers on public.financialstatements.ticker_id=public.tickers.id
inner join public.sectors on public.tickers.sector_id = public.sectors.id
inner join public.prices on public.prices.ticker_id=public.financialstatements.ticker_id
where prices.price_date = (select max(price_date) from prices where prices.ticker_id=financialstatements.ticker_id);