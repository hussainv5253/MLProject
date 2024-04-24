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

        # Pass the list of tuples (timestamp, power_value) to the HTML template
        predictions = [(str(timestamp), power_value) for timestamp, power_value in y_pred.items()]

        return render_template('index.html', predictions=predictions)
    else:
        return render_template('index.html', predictions=None)

if __name__ == '__main__':
    app.run(debug=True)
