from flask import Flask,render_template,redirect,request
from sklearn.externals import joblib
app=Flask(__name__)

model=joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')


    
@app.route('/' ,methods=["POST"])
def get_marks():
    if request.method == 'POST':
        hours=float(request.form['hours'])

        marks=str(model.predict([[hours]])[0][0])
        print(marks,hours)
    return render_template('index.html',your_mark=marks)

    


if __name__=='__main__':
    app.run(debug=True) 