# Heart Disease Prediction ❤️

A machine learning web app that predicts the risk of heart disease based on clinical parameters. Built with **Logistic Regression** (best performing model) and deployed via **Streamlit**.

---

## Live Demo

> Deploy on [[Streamlit Cloud](https://streamlit.io/cloud)](https://heart-disease--prediction.streamlit.app) — see setup instructions below.

---

## Project Overview

This project trains and compares 5 classification models on the [Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) and deploys the best-performing model as an interactive web app.

### Model Comparison Results

| Model | Accuracy | F1 Score |
|---|---|---|
| **Logistic Regression** | **86.96%** | **88.57%** |
| K-Nearest Neighbors | 86.41% | 88.15% |
| Naive Bayes | 85.33% | 86.83% |
| Support Vector Machine | 84.78% | 86.79% |
| Decision Tree | 78.26% | 80.39% |

✅ Logistic Regression selected as the final model.

---

## Features

- 11 clinical input features (age, cholesterol, resting BP, ECG results, etc.)
- Real-time prediction with a clean Streamlit UI
- Preprocessing pipeline with StandardScaler and one-hot encoding
- Model artifacts saved with `joblib` for fast loading

---

## Tech Stack

- **Python 3.11**
- **pandas**, **scikit-learn** — data processing & modeling
- **Streamlit** — web app UI
- **joblib** — model serialization
- **Google Colab** — training environment

---

## Project Structure

```
heart-disease-prediction/
│
├── app.py                    # Streamlit web application
├── Heart_disease.ipynb       # Full EDA, training & model comparison notebook
├── heart.csv                 # Dataset
│
├── LogisticRegression.pkl    # Trained Logistic Regression model
├── KNN.pkl                   # Trained KNN model (alternative)
├── scaler.pkl                # Fitted StandardScaler
├── columns.pkl               # Expected feature columns for inference
│
├── requirements.txt          # Python dependencies
└── README.md
```

---

## Input Features

| Feature | Description |
|---|---|
| Age | Age of the patient (18–100) |
| Sex | Male / Female |
| Chest Pain Type | Typical Angina, Atypical Angina, Non-anginal Pain, Asymptomatic |
| Resting Blood Pressure | In mm Hg |
| Cholesterol | Serum cholesterol in mg/dl |
| Fasting Blood Sugar | > 120 mg/dl: Yes / No |
| Resting ECG | Normal, ST-T wave abnormality, Left ventricular hypertrophy |
| Max Heart Rate | Maximum heart rate achieved |
| Exercise-Induced Angina | Yes / No |
| Oldpeak | ST depression induced by exercise |
| ST Slope | Up, Flat, Down |

---

## Setup & Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/priyanshu812/heart-disease-prediction.git
cd heart-disease-prediction
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## Deploy on Streamlit Cloud

1. Push this repo to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → New app
3. Select your repo, set `app.py` as the main file
4. Click **Deploy** — done!

---

## Dataset

**Heart Failure Prediction Dataset** by fedesoriano  
Source: [Kaggle](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)  
918 records, 12 features, binary target (`HeartDisease`: 0 or 1)

---

## Author

**Priyanshu Soni**  
B.Tech CSE (AI/ML) — Jain (Deemed-to-be University), Bangalore  
[LinkedIn](https://linkedin.com/in/priyanshu-soni-ai) · [GitHub](https://github.com/priyanshu812) · priyanshu812@gmail.com
