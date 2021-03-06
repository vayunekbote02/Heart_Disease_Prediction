import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [[float(x) for x in request.form.values()]]
    final_features = np.asarray(int_features)
    prediction = model.predict(final_features)
    if prediction == 1:
        return render_template('index.html', prediction_text='There is a chance that the patient might die.')
    else:
        return render_template('index.html', prediction_text='There is a low chance of the patient dying.')


if __name__ == "__main__":
    app.run(debug=True)
