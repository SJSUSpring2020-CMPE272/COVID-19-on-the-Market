import pandas as pd
from datetime import date

INITIAL_DATE = '2019-01-01' #initial date. constant. the tables will be truncated to this value

#verify the dataframes by printing to console
def output_to_terminal(df):
    print(df)
    print(df.dtypes)
    print("\n")

#truncate data points to after a certain date and set the date column as the index. Note that this requires the first column of the input date to be date
def set_index_and_truncate(df):
    df = df.set_index(df.columns[0]) #set the first column (date) as the index column
    df = df[(df.index > INITIAL_DATE)]
    return df

#read spread data
def parse_from_file():
    
    #dataframe definitions
        #dates - holds all date values from the INITIAL_DATE to today. serves as an index to join the other dataframes on to
        #sp500 - S&P500_index_daily_^GSPC
        #dji - DJI_index_daily_^dji
        #nasdaq - Nasdaq_index_daily_^IXIC
        #dgs10 - 10-year-treasury_constant_maturity_rate_daily_DGS10
        #t10ye - 10-year_breakeven_inflation_rate_daily_T10YIE
        #infection - Covid-19_daily_infection_statstics-US
        #unemp - Weekly_national_initial_unemployment_claims_seasonally_adjusted
        #petroleum - Weekly_national_gasoline_and_diesel_prices

    global dates, sp500, dji, nasdaq, w5000, dgs10, t10ye, infection, unemp, petroleum #set these as golbal for further manipulation from outside this function

    dates = pd.DataFrame(pd.date_range(INITIAL_DATE, date.today()))
    dates = set_index_and_truncate(dates)
    output_to_terminal(dates)

    sp500 = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\S&P500_index_daily_^GSPC.csv', parse_dates=[0]) #read data amd convert column 0 to datetime data type. For some docs it was parsed as a string data type otherwise
    sp500 = set_index_and_truncate(sp500)
    output_to_terminal(sp500)

    dji = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\DJI_index_daily_^dji.csv', parse_dates=[0])
    dji = set_index_and_truncate(dji)
    output_to_terminal(dji)

    nasdaq = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\Nasdaq_index_daily_^IXIC.csv', parse_dates=[0])
    nasdaq = set_index_and_truncate(nasdaq)
    output_to_terminal(nasdaq)

    w5000 = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\Wilshire_5000_total_market_index_^W5000.csv', parse_dates=[0])
    w5000 = set_index_and_truncate(w5000)
    output_to_terminal(w5000)

    dgs10 = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\10-year_treasury_constant_maturity_rate_DGS10.csv', parse_dates=[0])
    dgs10 = set_index_and_truncate(dgs10)
    output_to_terminal(dgs10)

    t10ye = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\10-year_breakeven_inflation_rate_T10YIE.csv', parse_dates=[0])
    t10ye = set_index_and_truncate(t10ye)
    output_to_terminal(t10ye)
    
    #remember to add an extra set of data on the top of the input csv (for one day earlier) to have 0 confirmed, 0 treated, and 0 dead. the backfill would extend the 1 confirmed all the way up otherwise
    infection = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\covid-19_daily_infection_statstics-US.csv', parse_dates=[0])
    infection = set_index_and_truncate(infection)
    output_to_terminal(infection)

    unemp = pd.read_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\Weekly_national_initial_unemployment_claims_seasonally_adjusted.csv', parse_dates=[0])
    unemp = set_index_and_truncate(unemp)
    output_to_terminal(unemp)

    petroleum = pd.read_excel(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Data\Weekly_national_gasoline_and_diesel_prices.xlsx', parse_dates=[0])
    petroleum = set_index_and_truncate(petroleum)
    output_to_terminal(petroleum)

def merge_temporal_dataframes(df1, df2, time_tolerance):
    df3 = pd.merge_asof(df1, df2, left_on= df1.index, right_on = df2.index, tolerance=pd.Timedelta(time_tolerance), direction='nearest') # merge_asof like join but for temporal data. can set tolernaces for date disparities
    df3 = df3.set_index(df3.columns[0]) #set index to date again
    return df3

parse_from_file()

#there are gaps that exist in the data. e.g: weekends for stock market data. the rest of the week for weekly data.

#the following have null values that need to be filled forward. 
df_output = merge_temporal_dataframes(dates,sp500,'0') # no tolerance. Exact match
df_output = merge_temporal_dataframes(df_output,dji,'0')
df_output = merge_temporal_dataframes(df_output,nasdaq,'0')
df_output = merge_temporal_dataframes(df_output,w5000,'0')
df_output = merge_temporal_dataframes(df_output,dgs10,'0')
df_output = merge_temporal_dataframes(df_output,t10ye,'0')
output_to_terminal(df_output) 

df_output = df_output.fillna(method='ffill') #fill the gaps with the previous non null value
output_to_terminal(df_output) 

#the following have null values that need to be filled backwards
df_output = merge_temporal_dataframes(df_output,infection,'0')
df_output = merge_temporal_dataframes(df_output,unemp,'0')
df_output = merge_temporal_dataframes(df_output,petroleum,'0')
output_to_terminal(df_output) 

df_output = df_output.fillna(method='bfill') #fill the gaps with the following non null value
output_to_terminal(df_output) 

#df_output = merge_temporal_dataframes(df_output,petroleum,'2D') # 2 day tolerance since the gasoline data is given each Monday and the unemployment data is given each Saturday

df_output.to_csv(r'E:\Github repo\COVID-19-on-the-Market\Pandas data processing\v2\Output\merged_data.csv')