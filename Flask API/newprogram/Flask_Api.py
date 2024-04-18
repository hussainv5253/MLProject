from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

df=20

@app.route('/one')
def hello_world():
   return "hello"

@app.route('/forecast/<farm_id><horizon>')
def forcasting_page(farm_id,horizon):
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
    return render_template("login2.html",result=data)



@app.route('/hello')
def hello_shubbu():
   return "<h1> Hiii Shubbuuuuuuu !!!!!! </h1>"


@app.route('/forecast',methods=['POST','GET'])
def login():
   if request.method=="POST":
      user= request.form['farm_id']
      user1= request.form['horizon']
      return redirect(url_for('forcasting_page',farm_id=user,horizon=user1))
   
   elif request.method=="GET":
      return render_template("index2.html")



if __name__ == '__main__':
   app.run(debug=True)