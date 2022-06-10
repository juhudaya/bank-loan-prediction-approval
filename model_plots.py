import pickle
import pandas as pd
import plotly.express as px
import plotly
import plotly.graph_objects as go
import plotly.express as px
import json

model = pickle.load(open('LogisticRegression.sav','rb'))

scaler_app = pickle.load(open('scalernormal_app.sav','rb'))
scaler_co = pickle.load(open('scalernormal_co.sav','rb'))
scaler_loanamount = pickle.load(open('scalernormal_loanamount.sav','rb'))
scaler_term = pickle.load(open('scalernormal_term.sav','rb'))


# import using pandas
df_main = pd.read_csv('loan.csv')
df_main = df_main.drop(['Loan_ID'],axis=1)
# df_dashboard = df_main.copy()

df_main
# -----------------------------

cols = ['ApplicantIncome', 
'CoapplicantIncome',
'LoanAmount', 
'Loan_Amount_Term', 
'Credit_History',
'Gender',
'Married',
'Dependents_0',
'Dependents_1',
'Dependents_2',
'Dependents_3+',
'Education',
'Self_Employed',
'Property_Area_Rural',
'Property_Area_Semiurban',
'Property_Area_Urban']



def predictions(data):
    output = []
    df = pd.DataFrame(data,index=[0])
    df = pd.get_dummies(df,columns=['Dependents','Property_Area'],drop_first=True)
    df = df.reindex(columns=cols,fill_value=0)
    df['ApplicantIncome'] = scaler_app.transform(df[['ApplicantIncome']])
    df['CoapplicantIncome'] = scaler_co.transform(df[['CoapplicantIncome']])
    df['LoanAmount'] = scaler_loanamount.transform(df[['LoanAmount']])
    #df['Loan_Amount_Term'] = scaler_term.transform(df[['Loan_Amount_Term']])
    pred_proba = model.predict_proba(df)
  
    # Adjust threshold
    pred_th = []
    for item in pred_proba[:,0]:
        if item > 0 :
            pred_th.append(0)
        else:
            pred_th.append(1)       
    pred = pred_th[0]

    # label
    if pred == 0 :
        output.append('HIGH RISK')
        output.append('REJECT LOAN')
        output.append([250,0,0])
    else :
        output.append('LOW RISK')
        output.append('LOAN ACCEPTED')
        output.append([0,0,250])
    return output

