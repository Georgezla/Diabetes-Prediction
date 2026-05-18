# Diabetes Prediction using Machine Learning

## Overview

This project predicts diabetes risk using supervised machine learning models trained on healthcare-related clinical data.

The workflow includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Model training and evaluation
* Cross-validation and hyperparameter tuning
* Deployment with Streamlit

---

## Dataset

The dataset contains medical features such as:

* Glucose
* Blood Pressure
* BMI
* Insulin
* Age
* Pregnancies
* Skin Thickness
* Diabetes Pedigree Function

Target:

* `0` → No diabetes
* `1` → Diabetes

---

## Models Used

* Logistic Regression
* Random Forest
* SVM
* Decision Tree

---

## Evaluation Metrics

Since this is a healthcare classification problem, the models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

Special attention was given to recall because false negatives in healthcare prediction can be critical.

---

## Results

| Model               | Accuracy | Recall | ROC-AUC |
| ------------------- | -------- | ------ | ------- |
| Logistic Regression | TBD      | TBD    | TBD     |
| Random Forest       | TBD      | TBD    | TBD     |
| XGBoost             | TBD      | TBD    | TBD     |

---

## Streamlit App

The project includes a Streamlit web application for real-time diabetes risk prediction.

Run locally:

```bash
streamlit run app.py
```

---

## Project Structure

```text
Diabetes-Prediction/
│
├── app.py
├── diabetes_model.pkl
├── requirements.txt
├── README.md
└── notebook.ipynb
```


## Author

George Zlakios
