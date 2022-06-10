from flask import Flask, render_template, request
import pandas as pd
from model_plots import predictions

# translate flask to python object
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('prediction.html')

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    
    # -------- prediction
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['Gender'] = int(data['Gender'])
        data['Married'] = int(data['Married'])
        data['Education'] = int(data['Education'])
        data['Self_Employed'] = int(data['Self_Employed'])
        data['ApplicantIncome'] = int(data['ApplicantIncome'])
        data['CoapplicantIncome'] = int(data['CoapplicantIncome'])
        data['LoanAmount'] = int(data['LoanAmount'])
        data['Loan_Amount_Term'] = int(data['Loan_Amount_Term'])
        data['Credit_History'] = int(data['Credit_History'])
     
        hasil = predictions(data)
        return render_template('result.html',data=data,prediction_status=hasil[0],prediction_loan=hasil[1],warna1=hasil[2][0],warna2=hasil[2][1],warna3=hasil[2][2])
    return render_template('prediction.html')




if __name__ == '__main__':
    app.run(debug=True,port=3000)