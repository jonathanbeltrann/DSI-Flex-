from flask import Flask, Response, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

## init the Flask app
app = Flask('myApp')

@app.route('/')
def home():
    return "Hello DSI Student! You are a webdev now"

name = 'Jon'
@app.route('/hc_page')
def hc_page():
    return f"""
    <html>
        <body>
        <h1> This is a hard coded HTML page </h1>
        <p> Here's the text. Isn't that cool {name}</p>
        </body>
    </html>
    """

@app.route('/hc_page.json')

def jason_data():
    favs = {
    "Movie": "Spiderman",
    "Band": "Linkin Park",
    "Song": "In the End"
    }
    return jsonify(favs), 200

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit')
def make_predictions():
    user_input = request.args

    X_test = np.array([int(user_input["OverallQual"]),
             int(user_input['FullBath']),
             int(user_input['GarageArea']),
             int(user_input["LotArea"])]).reshape(1,-1)

    model = pickle.load(open('models/model.p',"rb"))

    pred = model.predict(X_test)
    pred = pred[0]

    return render_template("Results.html", prediction=pred)
