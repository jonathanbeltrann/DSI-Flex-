from flask import Flask, Response, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# initialize the flask app
app = Flask("myApp")


# route 1: hello world
# return a string
@app.route("/")
def home():
    return "Hello DSI student! You rock!!!"


# route 2: return a webpage
# return hard-coded html
name = "Jeff"


@app.route("/hc_page")
def hc_page():
    return f"""
        <html>
            <body>
                <h1>This is a hard-coded page</h1>
                <p>Here's the text! {name}, isn't this cool? 🚀</p>
            </body>
        </html>
    """


# route 3: return some data in json format
# use jsonify function
@app.route("/hc_page.json")
def json_data():
    favs = {
        "Movie": "Zoolander",
        "Band": "Weezer",
        "Song": "The Middle",
        "Class": "DSIR-113020",
        "Height": 6,
    }
    return jsonify(favs), 200


# route 4: show user a form
@app.route("/form")
def form():
    return render_template("form.html")


# route 5: accept form submission and handle it
@app.route("/submit")
def make_predictions():

    # load in the form data from the incoming request
    user_input = request.args

    X_test = np.array(
        [
            int(user_input["OverallQual"]),
            int(user_input["FullBath"]),
            int(user_input["GarageArea"]),
            int(user_input["LotArea"]),
        ]
    ).reshape(1, -1)

    model = pickle.load(open("models/model.p", "rb"))
    pred = model.predict(X_test)
    pred = pred[0]

    return render_template("results.html", prediction=pred)


if __name__ == "__main__":
    app.run(debug=True)
