import pandas as pd 
import matplotlib.pyplot as plt 

#To read from Database
#Presently the dataset is already interms of months, so re-sampling not required.
"""
df=
train=
test=
"""

#Aggregating the dataset at daily level
df.Timestamp = pd.to_datetime(df.Datetime,format='%d-%m-%Y %H:%M') 
df.index = df.Timestamp 
df = df.resample('M').sum()
train.Timestamp = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
train.index = train.Timestamp 
train = train.resample('M').sum() 
test.Timestamp = pd.to_datetime(test.Datetime,format='%d-%m-%Y %H:%M') 
test.index = test.Timestamp 
test = test.resample('M').sum()

df.to_csv('monthly_preprocessed.csv', sep=',')



#Plotting data
train.Count.plot(figsize=(15,8), title= 'Monthly Forecast', fontsize=14)
test.Count.plot(figsize=(15,8), title= 'Monthly Forecast', fontsize=14)
plt.show()


