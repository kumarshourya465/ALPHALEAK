import pandas as pd

def process_nav_data(raw_data):

    #converting a list to dataframe
    df=pd.DataFrame(raw_data)

    #converting the data types of columns from string to numeric and fixed the data format
    df["nav"]=pd.to_numeric(df["nav"])
    df["date"]=pd.to_datetime(df["date"],format="%d-%m-%Y")

    # used it for sorting the date in ascending order , also reset the index because it can get confusing
    df=df.sort_values("date",ascending=True).reset_index(drop=True)
    
    #used for calculating the percentage change
    df["daily_returns"]=df["nav"].pct_change()
    df["daily_returns"]=df["daily_returns"].fillna(0.0)

    df.set_index("date",inplace=True)

    return df