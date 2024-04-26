from flask import Flask, request, render_template
from Forecasting import wind_farm_prediction
import datetime

app = Flask(__name__)
last_forecast_end_time = None
selected_farm_id = None
selected_horizon = None

@app.route('/')
def index():
    global selected_farm_id, selected_horizon
    # Initialize selected_farm_id and selected_horizon if they are None
    if selected_farm_id is None:
        selected_farm_id = 1
    if selected_horizon is None:
        selected_horizon = 6
    return render_template('index.html', predictions=None, farm_id=selected_farm_id, horizon=selected_horizon)

@app.route('/forecast', methods=['POST'])
def forecast():
    global last_forecast_end_time, selected_farm_id, selected_horizon
    
    if request.method == 'POST':
        farm_id = int(request.form['farm_id'])
        horizon = int(request.form['horizon'])
        
        # Update selected farm ID and horizon
        selected_farm_id = farm_id
        selected_horizon = horizon
        
        # Pass the last forecast end time to the wind_farm_prediction function
        predictions, last_forecast_end_time, plot_base64 = wind_farm_prediction(farm_id, horizon, last_forecast_end_time)

        # Extract timestamps and power values from the predictions
        timestamps = [timestamp for timestamp, _ in predictions]
        power_values = [power_value for _, power_value in predictions]

        # Combine timestamps and power values into a list of tuples
        predictions_data = list(zip(timestamps, power_values))

        # Prepare additional info
        additional_info = f"Wind Farm ID: {selected_farm_id}, Horizon: {selected_horizon} hours"

        return render_template('index.html', predictions=predictions_data, plot_base64=plot_base64, additional_info=additional_info, farm_id=selected_farm_id, horizon=selected_horizon)
    else:
        return render_template('index.html', predictions=None)

if __name__ == '__main__':
    app.run(debug=True)
