from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.statespace.sarimax import SARIMAX


def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())


def ma(data, col, train, test, frequency):
    y_hat_avg = test.copy()
    y_hat_avg['moving_avg_forecast'] = train[col].rolling(5).mean().iloc[-1]
    print('Rmse= ', rmse(test[col], y_hat_avg.moving_avg_forecast))
    plt.figure(figsize=(16,8))
    plt.plot(train[col], label='Train')
    plt.plot(test[col], label='Test')
    plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
    plt.legend(loc='best')
    #plt.show()
    plt.savefig(frequency+'ma.png')
    
    
    
def ewma(data, col, train, test, frequency):
    y_hat_avg = test.copy()
    fit2 = SimpleExpSmoothing(np.asarray(train[col])).fit(smoothing_level=0.6,optimized=False)
    y_hat_avg['SES'] = fit2.forecast(len(test))
    print('Rmse= ', rmse(test[col], y_hat_avg['SES']))
    plt.figure(figsize=(16,8))
    plt.plot(train[col], label='Train')
    plt.plot(test[col], label='Test')
    plt.plot(y_hat_avg['SES'], label='Exponential Smoothing')
    plt.legend(loc='best')
    plt.savefig(frequency+'ses.png')
    #plt.show()
    


def holt_winter(data, col, train, test, sp, t, s, frequency):
    """
    data- Entire Data Frame
    col- Target value
    train - Train Data Frame
    test - Test Data Frame
    sp - Seasonality period
    t - Trend - add/multiplicative
    s- Seasonal - add/multiplicative
    """
    y_hat_avg = test.copy()
    fit1 = ExponentialSmoothing(np.asarray(train[col]) ,seasonal_periods=sp ,trend=t, seasonal=s).fit()
    y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))

    #To print rms
    rms = rmse(test[col], y_hat_avg.Holt_Winter)
    print('RMSE', rms)

    #To plot the results
    plt.figure(figsize=(16,8))
    plt.plot( train[col],  label='Train')
    plt.plot(test[col], label='Test')
    plt.plot(y_hat_avg['Holt_Winter'], label='Holt_Winter')
    plt.legend(loc='best')
    plt.savefig(frequency+'holtswinter.png')
    #plt.show()


def sarima(data, col, train, test, order_val, s_ord, tr, frequency):
    """
    data - Entire Dataframe
    col - Target value
    train - Train Data Frame
    test - Test Data Frame
    order_val - (p,d,q)
    s_ord - (P,D,Q,s)
    tr =  str{‘n’,’c’,’t’,’ct’} or iterable, optional
    
    
    """
    
    y_hat_avg = test.copy()
    fit1 = SARIMAX(train[col], order=order_val,seasonal_order=s_ord, trend=tr ).fit()
    y_hat_avg['SARIMA'] = fit1.predict(start=train.index[-1], end=test.index[-1], dynamic=True)

    print('Rmse= ', rmse(test[col], y_hat_avg['SARIMA']))
    #print(y_hat_avg)
    plt.figure(figsize=(16,8))
    plt.plot( train[col], label='Train')
    plt.plot(test[col], label='Test')
    plt.plot(y_hat_avg['SARIMA'], label='SARIMA')
    plt.legend(loc='best')
    plt.savefig(frequency+'sarima.png')
    #plt.show()

