# Inorder to access Frontend web app, Run "streamlit run Streamlit_app.py"
import streamlit
import requests
import json
import pandas as pd
from functools import reduce


base_url = "http://backend_api:8000/"

required_columns = ['Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour',
                    'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
                    'Num_Credit_Card', 'Interest_Rate', 'Delay_from_due_date', 
                    'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 
                    'Num_Credit_Inquiries', 'Outstanding_Debt', 'Credit_History_Age',
                    'Amount_invested_monthly', 'Monthly_Balance']

loans_columns = ['Mortgage_Loan', 'Personal_Loan', 'Credit-Builder_Loan', 
        'Debt_Consolidation_Loan', 'Payday_Loan', 'Auto_Loan', 'Home_Equity_Loan',
        'Student_Loan', 'Not_Specified_Loan']

required_columns += loans_columns

def validate_data(df):
    return set(required_columns).issubset(df.columns)

def aggregate_num_loans():
    streamlit.session_state.num_of_loan = reduce(lambda x, y: x+y, 
                                                [streamlit.session_state[loan] \
                                                for loan in loans_columns])

def convert_df(df):
    return df.to_csv().encode('utf-8')


def run():

    streamlit.title("Credit Score Classifier 🤑💳💹💸")
    streamlit.header('From Data Entry')
    age = streamlit.number_input("Age", min_value=1, value=25, step=1)
    credit_mix = streamlit.selectbox('Credit Mix', ['Good', 'Standard', 'Bad'])
    payment_of_min_amount = streamlit.selectbox('Payment of Min Amount', ['No', 'Yes'])
    payment_behaviour = streamlit.selectbox('Payment Behaviour', 
                                                ['High_spent_Small_value_payments',
                                                'Low_spent_Large_value_payments',
                                                'Low_spent_Medium_value_payments',
                                                'Low_spent_Small_value_payments',
                                                'High_spent_Medium_value_payments',
                                                'High_spent_Large_value_payments'])
    annual_income = streamlit.number_input("Annual Income", value=50_500.00)
    monthly_inhand_salary = streamlit.number_input("Monthly Inhand Salary", 
                                                    min_value=0.0, value=4200.00)
    num_bank_accounts = streamlit.number_input("Num of Bank Accounts", min_value=0)
    num_credit_card = streamlit.number_input("Num Credit Card", 
                                            min_value=0, max_value=11)
    interest_rate = streamlit.number_input("Interest Rate", 
                                            min_value=1.0, max_value=34.0, step=0.5)
    delay_from_due_date = streamlit.number_input('Delay from Due Date', 
                                                min_value=0, max_value=67, step=1)
    num_of_delayed_payment = streamlit.number_input('Num of Delayed Payment', 
                                                min_value=0, max_value=28, step=1)
    changed_credit_limit = streamlit.number_input('Changed Credit Limit', 
                                                min_value=0.0, max_value=37.0, step=0.1)
    num_credit_inquiries = streamlit.number_input('Num Credit Inquiries', 
                                                    min_value=0, step=1)
    outstanding_debt = streamlit.number_input('Outstanding Debt', min_value=0)
    credit_history_age = streamlit.number_input('Credit History Age', 
                                                min_value=1, max_value=404, step=1)
    amount_invested_monthly = streamlit.number_input('Amount Invested Monthly', min_value=0)
    monthly_balance = streamlit.number_input('Monthly Balance', min_value=0)
    
    streamlit.divider()
    streamlit.subheader('Types of Loans')
    
    mortgage_loan = streamlit.number_input('Mortgage Loan', 
                                                min_value=0, step=1, key='mortgage_loan',
                                                on_change=aggregate_num_loans)
    personal_loan = streamlit.number_input('Personal Loan', 
                                                min_value=0, step=1, key='personal_loan',
                                                on_change=aggregate_num_loans)
    credit_builder_loan = streamlit.number_input('Credit Builder Loan', 
                                                min_value=0, step=1, 
                                                key='credit_builder_loan',
                                                on_change=aggregate_num_loans)
    debt_consolidation_loan = streamlit.number_input('Debt Consolidation Loan', 
                                                min_value=0, step=1, 
                                                key='debt_consolidation_loan',
                                                on_change=aggregate_num_loans)
    payday_loan = streamlit.number_input('Payday Loan', 
                                                min_value=0, step=1,
                                                key='payday_loan',
                                                on_change=aggregate_num_loans)
    auto_loan = streamlit.number_input('Auto Loan', 
                                                min_value=0, step=1, key='auto_loan',
                                                on_change=aggregate_num_loans)
    home_equity_loan = streamlit.number_input('Home Equity Loan', 
                                                min_value=0, step=1,
                                                key='home_equity_loan',
                                                on_change=aggregate_num_loans)
    student_loan = streamlit.number_input('Student Loan', 
                                                min_value=0, step=1, key='student_loan',
                                                on_change=aggregate_num_loans)
    not_specified_loan = streamlit.number_input('Not Specified Loan', 
                                                min_value=0, step=1,
                                                key='not_specified_loan',
                                                on_change=aggregate_num_loans)
    num_of_loan = streamlit.number_input("Num of Loan", 
                                        min_value=0, max_value=10, step=1,
                                        key='num_of_loan',
                                        disabled=True)
    data = { 
        'Age': age,
        'Credit_Mix': credit_mix,
        'Payment_of_Min_Amount': payment_of_min_amount,
        'Payment_Behaviour': payment_behaviour,
        'Annual_Income': annual_income,
        'Monthly_Inhand_Salary': monthly_inhand_salary,
        'Num_Bank_Accounts': num_bank_accounts,
        'Num_Credit_Card': num_credit_card,
        'Interest_Rate': interest_rate,
        'Num_of_Loan': num_of_loan,
        'Delay_from_due_date': delay_from_due_date,
        'Num_of_Delayed_Payment': num_of_delayed_payment,
        'Changed_Credit_Limit': changed_credit_limit,
        'Num_Credit_Inquiries': num_credit_inquiries,
        'Outstanding_Debt': outstanding_debt,
        'Credit_History_Age': credit_history_age,
        'Amount_invested_monthly': amount_invested_monthly,
        'Monthly_Balance': monthly_balance,
        'Mortgage_Loan': mortgage_loan,
        'Personal_Loan': personal_loan,
        'Credit-Builder_Loan': credit_builder_loan,
        'Debt_Consolidation_Loan': debt_consolidation_loan,
        'Payday_Loan': payday_loan,
        'Auto_Loan': auto_loan,
        'Not_Specified_Loan': not_specified_loan,
        'Home_Equity_Loan': home_equity_loan,
        'Student_Loan': student_loan
        }

    if streamlit.button("Predict", key='on_data'):
        backend_endpoint = "inference"
        response = requests.post(url=base_url+backend_endpoint, 
                                json=data)
        response_dict = json.loads(response.text)
        inference_value = response_dict["inference"]
        prediction = None
        status_display = streamlit.success
        
        if inference_value == 0:
            prediction = 'Poor'
            status_display = streamlit.error
        elif inference_value == 1:
            prediction = 'Standard'
            status_display = streamlit.warning
        elif inference_value == 2:
            prediction = 'Good'
        
        streamlit.subheader('Credict Score Prediction')
        status_display(prediction)

# *******************************************************************
    streamlit.divider()
    streamlit.header('From a File')
    csv_file = streamlit.file_uploader('Upload a csv file', 
                                        type='csv',
                                        key='csv_upload')
    data_uploaded = True if (csv_file is not None) else False
    
    if data_uploaded:
        df = pd.read_csv(csv_file)
        streamlit.dataframe(df.sample(5))
        data_is_valid = validate_data(df)
    
    predict_button = streamlit.button("Predict", key="on_file")
    
    if predict_button:
        with streamlit.spinner("Loading Inference, Please wait ..."):
            if not data_uploaded:
                streamlit.error("Upload a .csv file first")
            else:
                if data_is_valid:
                    backend_endpoint = "inference/file"
                    response = requests.post(url=base_url+backend_endpoint,
                                            files={"csv_file": csv_file.getvalue()})
                        
                    response_dict = json.loads(response.text)
                    df_copy = df.copy()
                    df_copy['Prediction'] = response_dict['predictions']
                    df_copy['Prediction'] = df_copy['Prediction'].map({0: 'Poor',
                                                                1: 'Standard', 
                                                                2: 'Good'})
                    csv = convert_df(df_copy[['Prediction']])
                    
                    # **************************************************************
                    streamlit.divider()
                    streamlit.header('Predictions')
                    streamlit.dataframe(df_copy)
                    
                    _ , mid_col, _ = streamlit.columns(3)
                    with mid_col: 
                        streamlit.download_button('Download Predictions Only', 
                                                csv, 
                                                'predictions.csv',
                                                'text/csv')
                else:
                    streamlit.error(f'''The columns in the uploaded file does not match \
the expected columns for the model.   
Please upload a compatible data file.The data should contain the following columns:   
{required_columns}''')


if __name__ == '__main__':
    #by default it will run at 8501 port
    run()