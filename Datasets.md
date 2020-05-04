## Datasets: 

File name										Source																	Last updated

covid-19_daily_infection_statstics-US	-						https://datahub.io/core/covid-19#readme													5/3/2020

Weekly_national_initial_unemployment_claims_seasonally_adjusted	-			https://fred.stlouisfed.org/series/ICSA													5/3/2020

Weekly_national_gasoline_and_diesel_prices	-					https://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_nus_w.htm											5/3/2020

S&P500_index_daily_^GSPC	-							https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC										5/3/2020

DJI_index_daily_^DJI	-								https://finance.yahoo.com/quote/%5EDJI/history?p=%5EDJI											5/3/2020

Nasdaq_index_daily_^IXIC	-							https://finance.yahoo.com/quote/%5EIXIC/history?p=%5EIXIC										5/3/2020

Wilshire_5000_total_market_index_^W5000		-					https://finance.yahoo.com/quote/%5EW5000/history?p=%5EW5000										5/3/2020

10-year-treasury_constant_maturity_rate_DGS10	-					https://fred.stlouisfed.org/series/DGS10												5/3/2020

10-year_breakeven_inflation_rate_T10YIE		-					https://fred.stlouisfed.org/series/T10YIE												5/3/2020

We combined multiple datasets into one large dataset to use to train our model. The reason being is that there is no pregenerated dataset relating the corona virus statistics with the various economic statistics. Thus, in this project, we will have to make our own by stitching together these datasets. We are planning to get our data based on weeks starting in 2020, and do joins on the data to merge them together. 
