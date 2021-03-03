# app.py
 
from flask import Flask, render_template, request
import pickle
from sklearn.linear_model import LogisticRegression
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')
 
 
 
@app.route('/predict',methods=['POST'])
def predict():
 
    if request.method == 'POST':
 
        spl = request.form['spl']
        spw = request.form['spw']
        ptl = request.form['ptl']
        ptw = request.form['ptw']

        a = float(spl)
        b = float(spw)
        c = float(ptl)
        d = float(ptw)
        data =[[a,b,c,d]]
 
        lr = pickle.load(open('iris.pkl', 'rb'))
        prediction = lr.predict(data)[0]
 
    return render_template('index.html', prediction=prediction)
 
 
 
if __name__ == '__main__':
    app.run()