from flask import Flask, request, render_template
from Forecasting import wind_farm_prediction
import datetime

app = Flask(__name__)
last_forecast_end_time = None

@app.route('/')
def index():
    return render_template('index.html', predictions=None)

@app.route('/forecast', methods=['POST'])
def forecast():
    global last_forecast_end_time
    
    if request.method == 'POST':
        farm_id = int(request.form['farm_id'])
        horizon = int(request.form['horizon'])
        
        # Pass the last forecast end time to the wind_farm_prediction function
        predictions, last_forecast_end_time = wind_farm_prediction(farm_id, horizon, last_forecast_end_time)

        # Extract timestamps and power values from the predictions
        timestamps = [timestamp for timestamp, _ in predictions]
        power_values = [power_value for _, power_value in predictions]

        # Combine timestamps and power values into a list of tuples
        predictions_data = list(zip(timestamps, power_values))

        return render_template('index.html', predictions=predictions_data)
    else:
        return render_template('index.html', predictions=None)

if __name__ == '__main__':
    app.run(debug=True)