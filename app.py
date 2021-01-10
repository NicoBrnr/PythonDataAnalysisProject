import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#Load our model with pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#Home page of the site
@app.route('/')
def home():
    return render_template('index.html')

#Predict page
@app.route('/predict',methods=['POST'])
def predict():

    #Collect all the data of all the features of our model
    int_features = [int(x) for x in request.form.values()]
    #Put them in an array for json
    final_features = [np.array(int_features)]
    #Predict the output
    prediction = model.predict(final_features)

    #Round the prediction because a comment is an int obviously
    output = np.abs(round(prediction[0]))

    #Render the result 
    return render_template('index.html', prediction_text='Number of comments under the post : {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)