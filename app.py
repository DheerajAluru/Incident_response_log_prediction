from distutils.log import debug
from flask import Flask, render_template, flash, request, jsonify
import pickle
import joblib
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'form123'
app.debug = True



@app.route('/', methods=['GET', 'POST'])
def home():

    # to_predict_list = request.form.to_dict()
    # to_predict_list = list(to_predict_list.values())
    # to_predict_list = np.array(list(map(float, to_predict_list))).reshape(1, 2)
    # form=PredForm()
    # prediction = model.predict(to_predict_list)
    # print(list(prediction))
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predic():
    with open('data/model_tr2', 'rb') as f:
        model = pickle.load(f)
    features_data=[str(x) for x in request.form.values()]
    final_feat=[np.array(features_data)]
    prediction=model.predict(final_feat)
    return render_template('index.html', predict_txt='Predicted Finish Time in Days: {}'.format((prediction)))

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080)