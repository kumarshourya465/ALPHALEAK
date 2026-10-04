import pandas as pd
import numpy as np

def process_nav_data(raw_data):

    #converting a list to dataframe
    df=pd.DataFrame(raw_data)

    #converting the data types of columns from string to numeric and fixed the data format
    df["nav"]=pd.to_numeric(df["nav"])
    df=df[df["nav"]>0]
    df["date"]=pd.to_datetime(df["date"],format="%d-%m-%Y")

    # used it for sorting the date in ascending order , also reset the index because it can get confusing
    df=df.sort_values("date",ascending=True).reset_index(drop=True)
    
    #used for calculating the percentage change
    df["daily_returns"]=(df["nav"].pct_change()).replace([np.inf,-np.inf],np.nan)
    df["daily_returns"]=df["daily_returns"].fillna(0.0)

    #used for calculating simple moving average for 7 days.
    df["nav_7d_sma"]=((df["nav"].rolling(window=7)).mean()).fillna(0.0)

    df.set_index("date",inplace=True)

    return df

def get_summary_data(df):
    #calculating the total return, mean and the volatility(risk)
    #i used iloc specific to the column as well
    total_return=float((df["nav"].iloc[-1]-df["nav"].iloc[0])/df["nav"].iloc[0])
    average_daily_return=float(df["daily_returns"].mean())
    volatility=float(df["daily_returns"].std())


    best_day = float(df["daily_returns"].max())
    worst_day = float(df["daily_returns"].min())

    best_day_date=df.loc[df["daily_returns"]==best_day]
    worst_day_date=df.loc[df["daily_returns"]==worst_day]

    #finding the best_day and worst_day
    # print("best_day_date :",(best_day_date.index[-1]).strftime("%Y-%m-%d"))
    # print("worst_day_date:",(worst_day_date.index[-1]).strftime("%Y-%m-%d"))

    #print((df["daily_returns"]>0))
    win_rate = float((df["daily_returns"]>0).mean())

    peak=df["nav"].cummax()
    drawdown_series=(df["nav"]-peak)/peak
    max_drawdown=float(drawdown_series.min())


    #converting the above details into a dictionary, for easy access
    summary_data={"total_return":round(total_return,6),
                 "average_daily_return":round(average_daily_return,6),
                 "volatility":round(volatility,6),
                 "best_day":round(best_day,6),
                 "best_day_date":(best_day_date.index[-1]).strftime("%Y-%m-%d"),
                 "worst_day":round(worst_day,6),
                 "worst_day_date":(worst_day_date.index[-1]).strftime("%Y-%m-%d"),
                 "max_drawdown":round(max_drawdown,6),
                 "win_rate":round(win_rate,6)}
    return summary_data
