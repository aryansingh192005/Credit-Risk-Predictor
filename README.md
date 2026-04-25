# 💳 Credit Risk Predictor

A machine learning web app that predicts whether a loan applicant is likely to default, built with Python and deployed using Streamlit.

🔗 **Live App**: [Click here to try it](https://credit-risk-predictor-u59h8ymqgrlsyb2dwbuauk.streamlit.app/)

---

## 📌 Project Overview

This project uses a Logistic Regression model trained on a credit risk dataset to classify applicants as high or low default risk based on their financial and personal profile.

---

## 📊 Dataset

- 1,000 applicant records
- 7 features: Age, Income, Loan Amount, Credit Score, Employment Years, Education Level, Housing Status
- Target: Default (1 = defaulted, 0 = did not default)
- Class imbalance: 86% non-default, 14% default

---

## ⚙️ How It Works

1. User enters applicant details in the web app
2. Data is preprocessed (scaled + encoded)
3. Model predicts default probability
4. Result shown as High Risk or Low Risk

---

## 📈 Model Performance

| Metric    | Score |
|-----------|-------|
| Accuracy  | 0.58  |
| Precision | 0.20  |
| Recall    | 0.55  |

> Recall is prioritized over accuracy due to class imbalance.

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 🚀 Run Locally

```bash
git clone https://github.com/yourusername/credit-risk-predictor
cd credit-risk-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 👤 Author

Made by [Aryan Singh] — connect with me on [LinkedIn](linkedin.com/in/aryansingh192005)
