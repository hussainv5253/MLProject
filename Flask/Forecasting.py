import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
import xgboost as xgb

def wind_farm_prediction(wind_farm_ID, horizon):

    if wind_farm_ID == 1:
        DATA_PATH = 'https://github.com/Bob05757/Renewable-energy-generation-input-feature-variables-analysis/raw/main/data_processed/wind_farms/Wind%20farm%20site%201%20(Nominal%20capacity-99MW).xlsx'
        df_wf = pd.read_excel(os.path.join(DATA_PATH))
        df_wf.columns = ['time', 'WS_10', 'WD_10', 'WS_30', 'WD_30', 'WS_50', 'WD_50', 'WS_cen', 'WD_cen', 'Air_T', 'Air_P', 'Air_H', 'Power(MW)']
    elif wind_farm_ID == 2:
        DATA_PATH = 'https://github.com/Bob05757/Renewable-energy-generation-input-feature-variables-analysis/raw/main/data_processed/wind_farms/Wind%20farm%20site%202%20(Nominal%20capacity-200MW).xlsx'
        df_wf = pd.read_excel(os.path.join(DATA_PATH))
        df_wf.columns =  ['time', 'WS_10', 'WD_10', 'WS_30', 'WD_30', 'WS_50', 'WD_50', 'WS_cen', 'WD_cen', 'Air_T', 'Air_P', 'Power(MW)']
    elif wind_farm_ID == 3:
        DATA_PATH = 'https://github.com/Bob05757/Renewable-energy-generation-input-feature-variables-analysis/raw/main/data_processed/wind_farms/Wind%20farm%20site%203%20(Nominal%20capacity-99MW).xlsx'
        df_wf = pd.read_excel(os.path.join(DATA_PATH))
        df_wf.columns =  ['time', 'WS_10', 'WD_10', 'WS_30', 'WD_30', 'WS_50', 'WD_50', 'WS_cen', 'WD_cen', 'Air_T', 'Air_P', 'Air_H', 'Power(MW)']
    else:
        raise ValueError("Invalid wind_farm_ID. Please choose 1, 2, or 3.")

    df_wf.columns = [col.strip() for col in df_wf.columns]
    df_wf.set_index('time', inplace=True)
    df_wf = df_wf.asfreq('15min')

    df_wf['WD_cen_sin'] = np.abs(np.sin(np.radians(df_wf['WD_cen'])))

    one_month_range = df_wf.index.max() - pd.DateOffset(months=1)
    df_demo = df_wf[df_wf.index >= one_month_range]

    y_train = df_wf[['Power(MW)']]
    y_test = df_demo[['Power(MW)']]
    X_train = df_demo[['WS_cen', 'WD_cen_sin', 'Air_T']]
 
    forecast = []

    pred_range = horizon * 60 // 15

    forecaster = xgb.XGBRegressor(max_depth=3, learning_rate=0.11, n_estimators=62)
    forecaster.fit(X_train, y_train)

    for t in range(pred_range):
        y_pred = forecaster.predict(fh=1)
        forecaster.append(y_pred.iloc[0])
        forecaster.update(y_test.iloc[t:t+1])
    
    y_pred = pd.Series(forecast, index=y_test.index)
    mae = mean_absolute_error(y_test, y_pred)

    plt.plot(y_pred)
    plt.title(f'Predictions for Wind farm {wind_farm_ID} (Next: {horizon} hours)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.savefig('predictions_plot.png')

    return y_pred, mae, 'predictions_plot.png'