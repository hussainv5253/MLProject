from flask import Flask, request, render_template
from Forecasting import wind_farm_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', predictions=None)

@app.route('/forecast', methods=['POST'])
def forecast():
    if request.method == 'POST':
        farm_id = int(request.form['farm_id'])
        horizon = int(request.form['horizon'])
        y_pred = wind_farm_prediction(farm_id, horizon)

        # Extract timestamps and power values from the predictions
        timestamps = [timestamp for timestamp, _ in y_pred]
        power_values = [power_value for _, power_value in y_pred]

        # Combine timestamps and power values into a list of tuples
        predictions = list(zip(timestamps, power_values))

        return render_template('index.html', predictions=predictions)
    else:
        return render_template('index.html', predictions=None)

if __name__ == '__main__':
    app.run(debug=True)
