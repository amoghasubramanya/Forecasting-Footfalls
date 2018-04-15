import pandas as pd
import Models
import ARIMAModelGrid

df_data_1=pd.read_csv('daily_preprocessed.csv')
train_df=df_data_1[:433]
test_df=df_data_1[433:444]

#import sys
#sys.stdout = open("F:\Projects\SJCE_HackOverflow\Finals\dailyresults.txt", "w")


print('Moving Average')
Models.ma(df_data_1, 'Count', train_df, test_df, 'Dailyplots/')
print('-------------------------------------------------------------------------------------------------------------')

print("Exponential Smoothing")
Models.ewma(df_data_1, 'Count', train_df, test_df, 'Dailyplots/')
print('-------------------------------------------------------------------------------------------------------------')

print("Holt's Winter")
Models.holt_winter(df_data_1, 'Count', train_df, test_df, 7, 'add', 'multiplicative', 'Dailyplots/')
print('-------------------------------------------------------------------------------------------------------------')

print("Seasonal ARIMA")
Models.sarima(df_data_1, 'Count', train_df, test_df, (2,2,4), (0,1,1,7), 't', 'Dailyplots/')
print('-------------------------------------------------------------------------------------------------------------')



print("ARIMA With Grid Search")
ARIMAModelGrid.arima_grid(df_data_1, 'Count', train_df, test_df, 'Dailyplots/')
print('-------------------------------------------------------------------------------------------------------------')
