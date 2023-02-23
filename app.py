import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

#Initialize the flask App
app = Flask(__name__)
#Load the pickled model and scaler
model = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template("home.html")

@app.route("/predict_api", methods=['POST'])
def predict_api():
    #Get the data from the POST request and store it in a variable
    data = request.json["data"]
    #Transfrom the data from json to 1D np array
    print(np.array(list(data.values())).reshape(1, -1))
    #Transform the data using the scaler
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    #Make a prediction using the model
    output = model.predict(new_data)
    print(output[0])
    #Return the prediction as json
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    print("I am in predict function ----------------------------------------")
    print(request.form.values())
    data=[float(x) for x in request.form.values()]
    print(data)
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))



if __name__ == '__main__':
    app.run(debug=True)