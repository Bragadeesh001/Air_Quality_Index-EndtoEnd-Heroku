import pickle
from flask import Flask,render_template,url_for,request,redirect

app=Flask(__name__)

#pickle
pickle_in=open('B:/MY_WORKS/PROJECT/Air quality index/rf_regresser.pkl','rb')
regresser=pickle.load(pickle_in)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction_page')
def prediction_page():
    return render_template('prediction.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    result=0.0
    if request.method=='POST':
        T=float(request.form['T'])
        TM=float(request.form['TM'])
        SLP=float(request.form['SLP'])
        H=float(request.form['H'])
        W=float(request.form['W'])
        V=float(request.form['V'])
        VM=float(request.form['VM'])
        result=regresser.predict([[T,TM,SLP,H,W,V,VM]])
    return render_template('prediction.html',result=result)





# to run
if __name__=='__main__':
    app.run(debug=True)