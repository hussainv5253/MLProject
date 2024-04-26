import pandas as pd
import xgboost as xgb

def wind_farm_prediction(wind_farm_ID, horizon, last_forecast_end_time=None):
    # Load the data based on the wind farm ID
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

    # Calculate the number of data points for one month
    num_data_points_in_one_month = 15 * 4 * 24 * 30

    # Use last_forecast_end_time if available
    if last_forecast_end_time is not None:
        # Update df_demo and df_train based on last_forecast_end_time
        df_demo = df_wf.loc[last_forecast_end_time:]
        df_train = df_wf.loc[:last_forecast_end_time]
    else:
        df_demo = df_wf.iloc[-num_data_points_in_one_month:]
        df_train = df_wf.iloc[10000:-num_data_points_in_one_month]

    y_train = df_train['Power(MW)']
    X_train = df_train[['WS_cen', 'WD_cen', 'Air_T']]
    
    y_test = df_demo[['Power(MW)']]
    X_test = df_demo[['WS_cen', 'WD_cen', 'Air_T']]

    # Initialize the XGBoost model
    xgboost_model = xgb.XGBRegressor(max_depth=10, learning_rate=0.11, n_estimators=62)

    # Initialize an empty list to store predictions and timestamps
    predictions = []
    timestamps = []

    # Iterate over each time step in the horizon
    for t in range(horizon*4):
        # Fit the initial model
        xgboost_model.fit(X_train, y_train)
        
        # Predict using the model
        prediction = xgboost_model.predict(X_test.iloc[[t]])

        # Append the prediction to the list of predictions
        predictions.append(prediction[0])

        # Store the corresponding timestamp
        timestamps.append(df_demo.index[t])

        # Remove the oldest row from X_train and y_train
        X_train = X_train.iloc[1:]
        y_train = y_train.iloc[1:]

        # Append the corresponding row from X_test to X_train and the prediction to y_train
        X_train = pd.concat([X_train, X_test.iloc[[t]]])
        y_train = pd.concat([y_train, pd.Series(prediction, index=[y_test.index[t]])])

    # Combine timestamps and predictions into a list of tuples
    result = list(zip(timestamps, predictions))

    # Return the end time of the forecast (last timestamp)
    end_time = timestamps[-1]

    return result, end_time