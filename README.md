# 👤 Gender Classification using Machine Learning

## 📌 Project Overview

This project predicts whether a person is **Male** or **Female** based on facial features using **Machine Learning**. The model is trained using the **Logistic Regression** algorithm and deployed with **Streamlit** for an interactive web application.

---

## 🚀 Features

- Predicts gender from facial features
- User-friendly Streamlit web application
- Data preprocessing using Label Encoding and StandardScaler
- Logistic Regression classification model
- Simple and interactive interface

---

## 📊 Dataset

The dataset contains the following features:

| Feature | Description |
|---------|-------------|
| Long Hair | Indicates whether the person has long hair |
| Forehead Width (cm) | Width of the forehead |
| Forehead Height (cm) | Height of the forehead |
| Nose Wide | Indicates whether the nose is wide |
| Nose Long | Indicates whether the nose is long |
| Thin Lips | Indicates whether the lips are thin |
| Distance Nose to Lip Long | Indicates whether the distance from nose to lip is long |
| Gender | Target Variable |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Label Encoding
4. Feature Scaling using StandardScaler
5. Train-Test Split
6. Model Training (Logistic Regression)
7. Model Evaluation
8. Model Deployment using Streamlit

---

## 📂 Project Structure

```
Gender-Classification/
│
├── app.py
├── gender_classification_v7.csv
├── logistic_regression_model.pkl
├── scaler.pkl
├── labelencoders.pkl
├── requirements.txt

```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Gender-Classification-ML.git
```

Go to the project folder:

```bash
cd Gender-Classification-ML
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Model

**Algorithm Used**

- Logistic Regression

**Preprocessing**

- Label Encoding
- StandardScaler

---

## 🎯 Prediction

The application predicts one of the following:

- Male 👨
- Female 👩

---




---

## ⭐ If you found this project helpful, give it a Star!
