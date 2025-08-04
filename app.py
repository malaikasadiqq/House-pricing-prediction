import pickle
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))   #loading the model
scaler=pickle.load(open('scaling.pkl','rb')) #loading the scaler

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    model_prediction = model.predict(new_data)
    print(model_prediction[0])
    return jsonify({'prediction': model_prediction[0]})

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input) 
    output = model.predict(final_input)[0]
    return render_template('home.html', prediction_text='The predicted house price value is {}'.format(output)) 



if __name__ == "__main__":
    app.run(debug=True)  