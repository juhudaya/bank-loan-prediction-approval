# bank-loan-prediction-approval

### 1. Data Preprocessing and Exploratory Data Analysis (EDA)
Started with import the dataset which is bank Loan dataset. 

👉 There are 13 variables in this data set:

8 categorical variables, 4 continuous variables, and 1 variable to accommodate the loan ID.

The following is the structure of the data set.

Variable Name Description Sample Data

    Loan_ID Loan reference number (unique ID) LP001002; LP001003; ...
    Gender Applicant gender (Male or Female) Male; Female
    Married Applicant marital status (Married or not married) Married; Not Married
    Dependents Number of family members 0; 1; 2; 3+
    Education Applicant education/qualification (graduate or not graduate) Graduate; Under Graduate
    Self_Employed Applicant employment status (yes for self-employed, no for employed/others) Yes; No
    ApplicantIncome Applicant's monthly salary/income 5849; 4583; ...
    CoapplicantIncome Additional applicant's monthly salary/income 1508; 2358; ...
    LoanAmount Loan amount 128; 66; ...
    Loan_Amount_Term The loan's repayment period (in days) 360; 120; ...
    Credit_History Records of previous credit history (0: bad credit history, 1: good credit history) 0; 1
    Property_Area The location of property (Rural/Semiurban/Urban) Rural; Semiurban; Urban
    Loan_Status Status of loan (Y: accepted, N: not accepted) Y; N


After that, I do data cleaning to remove some data, fixed nan value, remove the outlier, etc.

### 2. Modelling
I started modelling with standardize the continues data, doing cross validation method from five algorithms which are Logistic Regression, Decission Tree, Random Forest, Light GBM, and KNN for normal data and oversampling data (using SMOTE). Logisitic regression is the best algorithms which are from normal data (without SMOTE). In the following below is the result from cross validation :

![modelling](https://user-images.githubusercontent.com/101268442/173072099-e7fe22c0-7674-4b65-b37c-4c3160a2a104.png)Uploading modelling.png…]()



=============== CLASSIFICATION REPORT ===============
              precision    recall  f1-score   support

           0       0.90      0.41      0.56        64
           1       0.76      0.98      0.85       121

    accuracy                           0.78       185
   macro avg       0.83      0.69      0.71       185
weighted avg       0.80      0.78      0.75       185


tn :  26  fp :  38  fn :  3  tp :  118




### 3. Dashboard
The last i deploy the model in flask. 




![bank](https://user-images.githubusercontent.com/101268442/173077799-7a87b9f0-99fe-4bde-9540-152437a6e83d.png)


![prediction](https://user-images.githubusercontent.com/101268442/173075764-43963059-5421-4f4a-9d3e-ecef146afdcd.png)

