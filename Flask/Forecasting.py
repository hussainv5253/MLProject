import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sktime.forecasting.arima import ARIMA

def wind_farm_prediction(wind_farm_ID, horizon):
    if wind_farm_ID == 1:
        DATA_PATH = 'https://github.com/Bob05757/Renewable-energy-generation-input-feature-variables-analysis/raw/main/data_processed/wind_farms/Wind%20farm%20site%201%20(Nominal%20capacity-99MW).xlsx'
        df_wf = pd.read_excel(DATA_PATH)
        df_wf.columns = ['time', 'WS_10', 'WD_10', 'WS_30', 'WD_30', 'WS_50', 'WD_50', 'WS_cen', 'WD_cen', 'Air_T', 'Air_P', 'Air_H', 'Power(MW)']
    elif wind_farm_ID == 2:
        DATA_PATH = 'https://github.com/Bob05757/Renewable-energy-generation-input-feature-variables-analysis/raw/main/data_processed/wind_farms/Wind%20farm%20site%202%20(Nominal%20capacity-200MW).xlsx'
        df_wf = pd.read_excel(DATA_PATH)
        df_wf.columns =  ['time', 'WS_10', 'WD_10', 'WS_30', 'WD_30', 'WS_50', 'WD_50', 'WS_cen', 'WD_cen', 'Air_T', 'Air_P', 'Power(MW)']
    elif wind_farm_ID == 3:
        DATA_PATH = 'https://github.com/Bob05757/Renewable-energy-generation-input-feature-variables-analysis/raw/main/data_processed/wind_farms/Wind%20farm%20site%203%20(Nominal%20capacity-99MW).xlsx'
        df_wf = pd.read_excel(DATA_PATH)
        df_wf.columns =  ['time', 'WS_10', 'WD_10', 'WS_30', 'WD_30', 'WS_50', 'WD_50', 'WS_cen', 'WD_cen', 'Air_T', 'Air_P', 'Air_H', 'Power(MW)']
    else:
        raise ValueError("Invalid wind_farm_ID. Please choose 1, 2, or 3.")

    df_wf.columns = [col.strip() for col in df_wf.columns]
    df_wf.set_index('time', inplace=True)
    df_wf = df_wf.asfreq('15min')

    one_month_range = df_wf.index.max() - pd.DateOffset(months=1)
    df_demo = df_wf[df_wf.index >= one_month_range]

    y_train = df_wf['Power(MW)']
    y_test = df_demo[['Power(MW)']]

    forecast = []
    pred_range = horizon * 60 // 15 

    history = np.array(y_train)

    for t in range(pred_range):
        model = ARIMA(order=(1, 0, 1))
        model.fit(history)
        output = model.predict(fh=1)

        if isinstance(output, pd.DataFrame):
            forecast_value = output.iloc[0, 0]
        else:
            forecast_value = output[0, 0] if len(output.shape) == 2 else output[0]

        forecast.append(forecast_value)
        history = np.append(history, forecast_value)

    y_pred = pd.Series(forecast, index=y_test.index[:pred_range])

    return y_pred
