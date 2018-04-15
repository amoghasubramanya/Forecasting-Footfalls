import pandas as pd
import Models
import ARIMAModelGrid

#import sys
#sys.stdout = open("F:\Projects\SJCE_HackOverflow\Finals\monthlyresults.txt", "w")



df_data_2=pd.read_csv('monthly_preprocessed.csv')

train_df2=df_data_2[:133]
test_df2=df_data_2[133:]

print('Moving Average')
Models.ma(df_data_2, 'Count', train_df2, test_df2, 'Monthlyplots/')
print('-------------------------------------------------------------------------------------------------------------')

print("Exponential Smoothing")
Models.ewma(df_data_2, 'Count', train_df2, test_df2, 'Monthlyplots/')
print('-------------------------------------------------------------------------------------------------------------')

print("Holt's Winter")
Models.holt_winter(df_data_2, 'Count', train_df2, test_df2, 10, 'multiplicative', 'multiplicative', 'Monthlyplots/')
print('-------------------------------------------------------------------------------------------------------------')




print("Seasonal ARIMA")
Models.sarima(df_data_2, 'Count', train_df2, test_df2, (2,2,5), (1,1,1,1), 't', 'Monthlyplots/')
print('-------------------------------------------------------------------------------------------------------------')



print("ARIMA With Grid Search")
ARIMAModelGrid.arima_grid(df_data_2, 'Count', train_df2, test_df2, 'Monthlyplots/')
print('-------------------------------------------------------------------------------------------------------------')
