# 🧠 Emotion Detection System

An AI-powered Emotion Detection Web Application built using Natural Language Processing (NLP), Machine Learning, and Streamlit.

## 📌 Project Overview

This project analyzes user-entered text and predicts the underlying emotion using a Machine Learning model trained on an emotion-labeled dataset.

The application can identify the following emotions:

* 😊 Joy
* 😢 Sadness
* 😡 Anger
* 😨 Fear
* ❤️ Love
* 😲 Surprise

## 🚀 Features

* Real-time emotion prediction
* Interactive Streamlit web interface
* Text preprocessing and feature extraction
* Machine Learning-based classification
* Confidence score visualization
* User-friendly and responsive UI

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-Learn
* Logistic Regression
* CountVectorizer
* Pandas
* NumPy
* Joblib

## 📊 Machine Learning Workflow

1. Data Collection
2. Text Cleaning & Preprocessing
3. Feature Extraction using CountVectorizer
4. Model Training using Logistic Regression
5. Model Evaluation
6. Streamlit Web App Deployment

## 📁 Project Structure

```text
Emotion-Detection-System/
│
├── App.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/1vinay0056/Emotion-Detection-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run App.py
```

## 🎯 Sample Prediction

**Input:**

```text
I am feeling very happy and excited today!
```

**Output:**

```text
😊 Joy
```

## 👨‍💻 Author

**Vinay Kumar**

Computer Engineering Student | Data Analytics & Machine Learning Enthusiast

GitHub: https://github.com/1vinay0056

## ⭐ Future Improvements

* Deep Learning based emotion classification
* Emotion probability chart
* Emotion history tracking
* Multi-language support
* Cloud deployment
