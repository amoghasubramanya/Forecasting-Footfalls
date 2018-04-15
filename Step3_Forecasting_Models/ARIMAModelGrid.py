from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA, ARMAResults
from sklearn.metrics import mean_squared_error
from math import sqrt
import warnings
from matplotlib import pyplot 
import pandas as pd



def test_stationarity(timeseries):
      
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)

def arima_test(df, col):
    test_stationarity(df[col])   #Count

    plot_acf(df[col])            #Count
    pyplot.xlim(-1, 30)  
    pyplot.ylim(-1, 1)

    plot_pacf(df[col])            #Count
    pyplot.xlim(-1, 30)  
    pyplot.ylim(-1, 1) 

def arima_model(data, params):
    """
      data is a series of data points
      params tuple of (p, d, q) for the ARIMA model.  
    
    """
    data = data.astype('float32')   
    # train / test split, 90/10
    train_size = int(len(data) * 0.90)
    train, test = data[0:train_size], data[train_size:]
    history = [x for x in train]
    predictions = []
       
    for i in range(len(test)):
        arima_model = ARIMA(history, order = params)
        arima_model_fit = arima_model.fit(disp=0)
        y_forecast = arima_model_fit.forecast()[0]
        predictions.append(y_forecast)
        history.append(test.iloc[i])
    mse =  mean_squared_error(test, predictions)
    rmse = sqrt(mse)
    output_dict = {}
    output_dict = {'RMSE':rmse, 'ARIMA_MODEL': arima_model_fit, 'PARAMS': params}
    return output_dict


def arima_grid(df, col, train_df, test_df, frequency):
    p_values = range(0, 3)
    d_values = range(0, 3)
    q_values = range(0, 3)

    length=len(df)
    # Grid search
    warnings.filterwarnings("ignore")
    out_list = []
    best_score, best_cfg, aic, bic = float("inf"), None, None, None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                try:
                    arima_result = arima_model(train_df[col], (p, d, q))
                    out_list.append(arima_result)
                    if arima_result['RMSE'] < best_score:
                        best_score, best_cfg, aic, bic = arima_result['RMSE'], arima_result['PARAMS'], arima_result['ARIMA_MODEL'].aic, arima_result['ARIMA_MODEL'].bic
                    print('PARAMS: {}, RMSE: {}, AIC: {}, BIC: {}'.format(arima_result['PARAMS'], arima_result['RMSE'], arima_result['ARIMA_MODEL'].aic, arima_result['ARIMA_MODEL'].bic))
                except:
                    continue



    # Validate - forecast the next 10 values
    # get the best model
    best_arima_model = arima_model(train_df[col], best_cfg)  #dur
    forecast_10 = best_arima_model['ARIMA_MODEL'].forecast(steps = 10)[0]
    # RMSE
    mse =  mean_squared_error(df[col][(length-10):], forecast_10) #dur
    rmse = sqrt(mse)
    print('RMSE: {}'.format(rmse))


    forecast=pd.DataFrame(forecast_10, index=range((len(df)-10),len(df)))
    pyplot.figure()
    pyplot.plot( train_df[col], label='Train')
    pyplot.plot(test_df[col], label='Test')
    pyplot.plot(forecast, color='red',label='ARIMA')
    pyplot.legend(loc='best')
    pyplot.savefig(frequency+'arima.png')

