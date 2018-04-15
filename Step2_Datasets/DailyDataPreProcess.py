import pandas as pd 
import matplotlib.pyplot as plt 

#Presently for the publicly available dataset.
df = pd.read_csv("F:\Projects\SJCE_HackOverflow\\daily_data.csv")

#Subsetting the dataset
train=df[0:10392] 
test=df[10392:10680]
df=df[0:10680]

#Aggregating the dataset at daily level
df.Timestamp = pd.to_datetime(df.Datetime,format='%d-%m-%Y %H:%M') 
df.index = df.Timestamp 
df = df.resample('D').sum()
train.Timestamp = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
train.index = train.Timestamp 
train = train.resample('D').sum() 
test.Timestamp = pd.to_datetime(test.Datetime,format='%d-%m-%Y %H:%M') 
test.index = test.Timestamp 
test = test.resample('D').sum()

df.to_csv('daily_preprocessed.csv', sep=',')



#Plotting data
train.Count.plot(figsize=(15,8), title= 'Daily Forecast', fontsize=14)
test.Count.plot(figsize=(15,8), title= 'Daily Forecast', fontsize=14)
plt.show()


