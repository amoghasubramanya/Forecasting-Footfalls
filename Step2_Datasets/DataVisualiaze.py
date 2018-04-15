import pandas as pd 
import matplotlib.pyplot as plt 


"""
#For Dataset1
df=pd.read_csv("F:\Projects\SJCE_HackOverflow\\daily_preprocessed.csv")
train=df[:433]
test=df[433:444]

#Plotting data
train.Count.plot(figsize=(15,8), title= 'Daily Forecast', fontsize=14)
test.Count.plot(figsize=(15,8), title= 'Daily Forecast', fontsize=14)
plt.show()

plt.figure()
df.Count.plot(style='k.')

"""


#For Dataset2
df=pd.read_csv("F:\Projects\SJCE_HackOverflow\\monthly_preprocessed.csv")
print(df)
df.plot(title='Monthly Forecast')
df.plot(style='k.',title='Monthly Forecast')