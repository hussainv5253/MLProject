from flask import Flask, request, render_template

app = Flask(__name__)

def get_model(farm_id):
    return f"Model for Farm {farm_id}"

def forecast_wind_power(model, horizon):
    return {"forecast": [10, 20, 30], "confidence_interval": [5, 10, 15]}

def calculate_error(forecast, actual):
    errors = [abs(f - a) for f, a in zip(forecast, actual)]
    return errors

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forecast', methods=['POST'])
def forecast():
    farm_id = int(request.form['farm_id'])
    horizon = int(request.form['horizon'])
    actual_data = [5, 15, 25]

    model = get_model(farm_id)
    result = forecast_wind_power(model, horizon)
    forecast_data = result['forecast']
    confidence_interval = result['confidence_interval']
    errors = calculate_error(forecast_data, actual_data)

    return render_template('result.html', forecast=forecast_data, 
                           confidence_interval=confidence_interval, errors=errors)

if __name__ == '__main__':
    app.run(debug=True)