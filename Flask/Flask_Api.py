from flask import Flask, request, render_template
from Forecasting import wind_farm_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    if request.method == 'POST':
        farm_id = int(request.form['farm_id'])
        horizon = int(request.form['horizon'])
        y_pred, mae, plot_filename = wind_farm_prediction(farm_id, horizon)

        # Pass the results to the template for rendering
        return render_template('prediction.html', y_pred=y_pred, mae=mae, plot_filename=plot_filename)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

"""
app = Flask(__name__)

@app.route('/forecast/<farm_id><horizon>')
def forcasting_page(farm_id, horizon):
    data = {
        'XGboot': {
            'farm_id': f'{df}',
            'horizon': 'value 2',
            'additional_column1': 'value 3',
            'additional_column2': 'value 4',
        },
        'Random Forest': {
            'farm_id': 'value 1',
            'horizon': 'value 2',
            'additional_column1': 'value 3',
            'additional_column2': 'value 4',
        },
        'Linear Regression': {
            'farm_id': 'value 1',
            'horizon': 'value 2',
            'additional_column1': 'value 3',
            'additional_column2': 'value 4',
        }
    }
    return render_template("login2.html", result=data)


@app.route('/forecast',methods=['POST','GET'])
def login():
   if request.method=="POST":
      user= request.form['farm_id']
      user1= request.form['horizon']
      return redirect(url_for('forcasting_page', farm_id=user, horizon=user1))
   
   elif request.method=="GET":
      return render_template("index2.html")



if __name__ == '__main__':
   app.run(debug=True)
"""