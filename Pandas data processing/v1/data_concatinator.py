import pandas as pd

#verify the dataframes by outputting to console
def output_to_terminal(df):
    print(df)
    print(df.dtypes)
    print("\n")

#truncate data points to after 2020-01-01
def set_index_and_truncate(df):
    df = df.set_index(df.columns[0]) #set the first column (date) as the index column
    df = df[(df.index > '2020-01-01')]
    return df

#read spread data
def parse_from_file():
    
    global df_infection, df_unemployment, df_unemployment_CA, df_CA_gasoline #set these as golbal for further manipulation from outside this function

    #spread_rate #remove the province column?
    df_infection = pd.read_csv(r'E:\YATHU SJSU\SJSU MSSE\Spring 2020\CMPE 272 project code\modified data\US_COVID-19_count_modified.csv', parse_dates=[0]) #read data amd convert column 0 to datetime data type. For some docs it was parsed as a string data type otherwise
    df_infection = set_index_and_truncate(df_infection)
    output_to_terminal(df_infection)

    #unemployment
    df_unemployment = pd.read_excel(r'E:\YATHU SJSU\SJSU MSSE\Spring 2020\CMPE 272 project code\modified data\r539cy_modified.xls', parse_dates=[0])
    df_unemployment = set_index_and_truncate(df_unemployment)
    output_to_terminal(df_unemployment)

    #unemployment in CA
    df_unemployment_CA = pd.read_excel(r'E:\YATHU SJSU\SJSU MSSE\Spring 2020\CMPE 272 project code\modified data\r539cy-CA_modified.xls', parse_dates=[0])
    df_unemployment_CA = set_index_and_truncate(df_unemployment_CA)
    output_to_terminal(df_unemployment_CA)

    #CA gasoline
    df_CA_gasoline = pd.read_excel(r'E:\YATHU SJSU\SJSU MSSE\Spring 2020\CMPE 272 project code\modified data\California_Gasoline_modified.xls', parse_dates=[0]) 
    df_CA_gasoline = set_index_and_truncate(df_CA_gasoline)
    df_CA_gasoline = df_CA_gasoline.sort_index() #sort by ascending order using the index (date). The original date was in descending order
    output_to_terminal(df_CA_gasoline)

def merge_temporal_dataframes(df1, df2, time_tolerance):
    df3 = pd.merge_asof(df1, df2, left_on= df1.index, right_on = df2.index, tolerance=pd.Timedelta(time_tolerance), direction='nearest') # merge_asof like join but for temporal data. can set tolernaces for date disparities
    df3 = df3.set_index(df3.columns[0]) #set index to date again
    return df3

parse_from_file()

df_output = merge_temporal_dataframes(df_unemployment,df_unemployment_CA,'0') # no tolerance. Exact match

df_output = merge_temporal_dataframes(df_output,df_infection,'0') # no tolerance. Exact match

df_output = merge_temporal_dataframes(df_output,df_CA_gasoline,'2D') # 2 day tolerance since the gasoline data is given each Monday and the unemployment data is given each Saturday

output_to_terminal(df_output)

df_output.to_csv(r'E:\YATHU SJSU\SJSU MSSE\Spring 2020\CMPE 272 project code\modified data\combined_data.csv')