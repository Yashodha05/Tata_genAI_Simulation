import streamlit as st
import joblib
import pandas as pd

import os
import json
from huggingface_hub import InferenceClient

os.environ["HF_TOKEN"] = "YOUR_TOKEN_KEY"

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

model = joblib.load("logistic_model.pkl")

st.set_page_config(
    page_title="FinGuard Agentic AI",
    layout="wide"
)


def preprocess_input():

    data = {
        "Age": age,
        "Income": income,
        "Credit_Score": credit_score,
        "Credit_Utilization": credit_utilization,
        "Missed_Payments": missed_payments,
        "Loan_Balance": loan_balance,
        "Debt_to_Income_Ratio": debt_to_income,
        "Account_Tenure": account_tenure,

        "Month_1": 0,
        "Month_2": 0,
        "Month_3": 0,
        "Month_4": 0,
        "Month_5": 0,
        "Month_6": 0,

        "Employment_Status_Retired": 0,
        "Employment_Status_Self-employed": 0,
        "Employment_Status_Unemployed": 0,

        "Credit_Card_Type_Gold": 0,
        "Credit_Card_Type_Platinum": 0,
        "Credit_Card_Type_Standard": 0,
        "Credit_Card_Type_Student": 0,

        "Location_Houston": 0,
        "Location_Los Angeles": 0,
        "Location_New York": 0,
        "Location_Phoenix": 0
    }

    # Employment
    if employment == "Self-employed":
        data["Employment_Status_Self-employed"] = 1

    elif employment == "Unemployed":
        data["Employment_Status_Unemployed"] = 1

    elif employment == "retired":
        data["Employment_Status_Retired"] = 1

    # Card Type
    if card == "Gold":
        data["Credit_Card_Type_Gold"] = 1

    elif card == "Platinum":
        data["Credit_Card_Type_Platinum"] = 1

    elif card == "Standard":
        data["Credit_Card_Type_Standard"] = 1

    elif card == "Student":
        data["Credit_Card_Type_Student"] = 1

    # Location
    if location == "Houston":
        data["Location_Houston"] = 1

    elif location == "Los Angeles":
        data["Location_Los Angeles"] = 1

    elif location == "New York":
        data["Location_New York"] = 1

    elif location == "Phoenix":
        data["Location_Phoenix"] = 1

    # Months
    for i, month in enumerate(months, start=1):

        if month == "On-time":
            value = 2

        elif month == "Late":
            value = 1

        else:
            value = 0

        data[f"Month_{i}"] = value

    return pd.DataFrame([data])

def generate_ai_report(customer_data, prediction, probability):

    prompt = f"""
You are an expert AI Collections Manager working for a financial institution.

Analyze the customer's complete financial profile together with the Machine Learning prediction.

Customer Profile:

{customer_data}

Machine Learning Prediction

Prediction: {prediction}

Probability of Delinquency: {probability:.2%}

Instructions:

1. Analyze the customer's financial condition.
2. Explain which customer attributes influenced your reasoning.
   Consider:
   - Credit Score
   - Income
   - Missed Payments
   - Credit Utilization
   - Debt-to-Income Ratio
   - Loan Balance
   - Employment Status
   - Payment History

3. Recommend the best next action for the collections team.
   Your recommendation should be personalized based on the customer's profile.

4. Write a professional email that can be sent to the customer.

5. Even if two customers have the same prediction probability, generate different analyses and recommendations if their financial profiles are different.

6. Return ONLY valid JSON in the following format:

{{
    "analysis": "",
    "recommendation": "",
    "email": ""
}}
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=600
    )

    answer = response.choices[0].message.content.strip()

    # Remove markdown if the model wraps JSON in ```json
    answer = answer.replace("```json", "").replace("```", "").strip()

    return json.loads(answer)

st.title("FinGuard Agentic AI")


st.subheader("Customer Delinquency Prediction System")

st.markdown("---")

st.header("Customer Details")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

income = st.number_input(
    "Annual Income",
    min_value=0,
    value=60000
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=700
)

credit_utilization = st.slider(
    "Credit Utilization",
    0.0,
    1.0,
    0.30
)

missed_payments = st.number_input(
    "Missed Payments",
    min_value=0,
    max_value=20,
    value=1
)
loan_balance = st.number_input(
    "Loan Balance",
    min_value=0,
    value=150000
)

debt_to_income = st.slider(
    "Debt-to-Income Ratio",
    0.0,
    1.0,
    0.30
)

account_tenure = st.number_input(
    "Account Tenure (Years)",
    min_value=0,
    max_value=50,
    value=5
)
employment = st.selectbox(
    "Employment Status",
    [
        "EMP",
        "Self-employed",
        "Unemployed",
        "retired"
    ]
)
card = st.selectbox(
    "Credit Card Type",
    [
        "Student",
        "Standard",
        "Gold",
        "Platinum",
        "Business"
    ]
)
location = st.selectbox(
    "Location",
    [
        "Chicago",
        "Houston",
        "Los Angeles",
        "New York",
        "Phoenix"
    ]
)
months = []

options = ["On-time", "Late", "Missed"]

for i in range(1,7):
    month = st.selectbox(
        f"Month {i}",
        options,
        key=f"m{i}"
    )
    months.append(month)
predict = st.button("Predict Risk")

if predict:

    input_df = preprocess_input()

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.success("Prediction Completed!")

    st.metric(
        "Probability of Delinquency",
        f"{probability:.2%}"
    )

    st.markdown("---")

    st.header("AI Collection Report")
    with st.spinner("AI is generating the collection report..."):

        customer_profile = f"""
        Age: {age}
        Income: {income}
        Credit Score: {credit_score}
        Credit Utilization: {credit_utilization}
        Missed Payments: {missed_payments}
        Loan Balance: {loan_balance}
        Debt To Income Ratio: {debt_to_income}
        Account Tenure: {account_tenure}

        Employment Status: {employment}
        Credit Card: {card}
        Location: {location}

        Payment History:
        Month 1: {months[0]}
        Month 2: {months[1]}
        Month 3: {months[2]}
        Month 4: {months[3]}
        Month 5: {months[4]}
        Month 6: {months[5]}
        """

        report = generate_ai_report(
            customer_profile,
            prediction,
            probability
        )

   
    st.subheader("Analysis")
    st.write(report["analysis"])

    st.subheader(" Recommendation")
    st.info(report["recommendation"])

    st.subheader("Customer Email")
    st.code(report["email"], language="text")