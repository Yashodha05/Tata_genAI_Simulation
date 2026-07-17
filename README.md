# Tata_genAI_Simulation

# FinGuard Agentic AI 
AI-Powered Customer Delinquency Prediction & Intelligent Collection Assistant

# Overview

FinGuard Agentic AI is an end-to-end Machine Learning and Generative AI application that predicts customer delinquency risk and generates personalized collection recommendations for financial institutions.

The system combines a Logistic Regression classification model with a Large Language Model (LLM) from Hugging Face to provide not only a probability of delinquency but also a detailed financial analysis, collection recommendation, and a professional customer email.

This project was built to demonstrate how Machine Learning and Large Language Models can work together in real-world financial applications.

# Features
Customer Delinquency Prediction
Machine Learning-based Risk Scoring
Personalized AI Financial Analysis
AI-generated Collection Recommendation
AI-generated Professional Customer Email
Interactive Streamlit Web Application
Dynamic Customer Profile Analysis
End-to-End ML + LLM Pipeline

# Application Workflow

Customer Inputs
        ->
Data Preprocessing
        ->
Logistic Regression Model
        ->
Probability of Delinquency
        ->
Customer Profile + ML Prediction
        ->
Hugging Face LLM
        ->
Financial Analysis

Recommendation

Professional Email

# Technology Stack
Programming Language
Python
Machine Learning
Scikit-learn
Logistic Regression
Random Forest (Model Comparison)
SMOTE (Handling Class Imbalance)
Data Processing
Pandas
NumPy
Model Persistence
Joblib
Frontend
Streamlit
Large Language Model
Hugging Face Inference API
Qwen 2.5 7B Instruct
API Integration
Hugging Face Hub
Other Libraries
JSON
OS

# Machine Learning Pipeline
Data Cleaning
Missing Value Handling
Feature Engineering
One-Hot Encoding
Model Training
Model Evaluation
SMOTE Oversampling
Model Serialization using Joblib

# AI Pipeline

After the ML model predicts the probability of delinquency:

Customer financial profile is prepared.
ML prediction and probability are combined with customer details.
A structured prompt is generated.
Prompt is sent to Hugging Face's Qwen LLM.
The LLM generates:
Financial Analysis
Personalized Recommendation
Professional Customer Email
The response is parsed as JSON.
Results are displayed in the Streamlit interface.

# Application Screenshots
Home Page


<img width="1920" height="1080" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/18231dfc-43ce-48af-8949-5af39f7e77fa" />



Customer Input Form



<img width="1920" height="1080" alt="Screenshot (8)" src="https://github.com/user-attachments/assets/b342ac63-5726-4136-982c-67b5513f1bd0" />






<img width="1920" height="1080" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/cce51b1b-65bc-4ae8-8814-db74310eb8a1" />




Prediction Result



<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/f17d33cc-eee0-4cff-9cb6-b6f508b8030a" />





AI Generated Analysis

AI Generated Recommendation

AI Generated Customer Email


<img width="1920" height="1080" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/bd0ced80-bde2-4fa8-ba1f-2b9a396b14d9" />



# Project Structure

FinGuard-Agentic-AI/
-app.py
-logistic_model.pkl
-random_forest.pkl
-requirements.txt
-README.md
-dataset

# Installation

Clone the repository

git clone- https://github.com/Yashodha05/Tata_genAI_Simulation

Navigate to the project

cd FinGuard-Agentic-AI

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py

# Sample Output

The application generates:

Probability of Delinquency
AI Financial Analysis
Personalized Recommendation
Professional Email

# Learning Outcomes

This project helped me understand:

Data Preprocessing
Feature Engineering
Logistic Regression
Random Forest
SMOTE
Model Evaluation
Model Serialization
Streamlit Development
API Integration
Prompt Engineering
Hugging Face Inference API
JSON Parsing
Building an end-to-end AI application

# Challenges Faced

During development, several challenges were encountered:

Highly imbalanced dataset (84:16 class ratio)
Models were biased toward the majority class
Logistic Regression initially predicted only the majority class
Random Forest also struggled with minority class detection
SMOTE was applied to improve minority class learning
Multiple prompt iterations were required to obtain consistent and structured LLM responses
JSON parsing issues from LLM outputs were resolved through prompt refinement and response cleaning

These challenges provided valuable insights into real-world machine learning limitations and model evaluation.

# Future Enhancements
Use a larger real-world credit risk dataset
Train advanced ML models (XGBoost, LightGBM, CatBoost)
Integrate Retrieval-Augmented Generation (RAG)
Add true multi-agent workflows using LangGraph
Store customer history in a database
Deploy the application on Streamlit Community Cloud
Improve model performance with additional features and hyperparameter tuning
Build a dashboard for collection officers

# Acknowledgement

This project was developed as a learning-oriented AI/ML application.

The core Machine Learning pipeline—including data preprocessing, feature engineering, model training, evaluation, and integration—was implemented by me.

While developing the Streamlit interface, Hugging Face LLM integration, prompt engineering, and JSON response handling, I leveraged Generative AI tools (ChatGPT) and official documentation to learn unfamiliar technologies and accelerate development. These resources served as learning aids, and the final application helped me gain practical experience in combining Machine Learning with Large Language Models.

# Author

Yashodha A

Computer Science Engineering Student (UVCE)

Interested in:

Artificial Intelligence
Machine Learning
Generative AI
Data Science
Intelligent Software Systems

I especially like the Acknowledgement section because it's transparent without underselling your work. It tells recruiters exactly what you built yourself, what you learned with assistance, and frames the project as a genuine learning experience rather than trying to claim expertise you don't yet have. That's the kind of honesty that builds credibility.
