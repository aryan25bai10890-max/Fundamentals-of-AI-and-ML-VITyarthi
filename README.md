# 🩺 AI Disease Prediction System

**Project Type:** Bring Your Own Project (BYOP) – Capstone Activity  
**Author:** Aryan Bardiya  
**Institution:** Vellore Institute of Technology (VIT)  
**Course:** Artificial Intelligence / Machine Learning  
**Academic Year:** 2026  

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)  
2. [Problem Statement](#problem-statement)  
3. [Objectives](#objectives)  
4. [Features](#features)  
5. [Dataset](#dataset)  
6. [Machine Learning Model](#machine-learning-model)  
7. [Installation & Setup](#installation--setup)  
8. [Usage](#usage)  
9. [Screenshots](#screenshots)  
10. [Project Architecture](#project-architecture)  
11. [Future Work](#future-work)  
12. [Disclaimer](#disclaimer)  
13. [References](#references)  

---

## 📌 Project Overview

The **AI Disease Prediction System** predicts possible diseases based on user-reported symptoms.

It demonstrates how **AI and Machine Learning concepts** can be applied to real-world healthcare challenges, helping users identify potential health conditions while encouraging timely medical consultation.

### 🛠️ Technologies Used

- Python  
- Streamlit  
- Scikit-Learn  
- Pandas  

---

## ❗ Problem Statement

Many people attempt self-diagnosis using internet searches, which can lead to misinformation or delayed treatment.

This project predicts diseases from symptom combinations using machine learning, providing preliminary insights while emphasizing professional medical consultation.

---

## 🎯 Objectives

- Predict diseases from symptoms using machine learning  
- Create a **user-friendly interface** for symptom input  
- Display **prediction confidence** (top 3 likely diseases)  
- Provide **disease information and suggested precautions**  
- Demonstrate **model evaluation metrics** (accuracy, precision, recall, F1-score)  

---

## ✨ Features

- **Multi-symptom input:** Select multiple symptoms from a sidebar  
- **Disease prediction:** Uses a trained Random Forest model  
- **Prediction confidence:** Displays probabilities for top 3 diseases  
- **Disease information panel:** Includes description and precautions  
- **Model performance dashboard:** Shows evaluation metrics  
- **Interactive & educational design**  

---

## 📊 Dataset

The model is trained on a **synthetic dataset** representing:

- 130+ symptoms (binary features)  
- 40 disease classes  
- 10,000+ samples simulating real-world symptom-disease relationships  

📁 Dataset location : dataset/Training.csv


---

## 🤖 Machine Learning Model

- **Algorithm:** Random Forest Classifier  

### 🔍 Why Random Forest?
- Handles high-dimensional data  
- Robust to overfitting  
- Provides probability estimates  

### ⚙️ Training Details
- Train/Test split: 80% / 20%  
- Saved model: model/rf_model.pkl


---

## ⚙️ Installation & Setup

### ✅ Prerequisites

- Python 3.10+  
- pip (Python package manager)  

### 📥 Clone Repository

```bash
git clone <your-repo-link>
cd disease_prediction_project
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run Application
```bash
streamlit run app.py

```


### 🚀 Usage

- Open the Streamlit app in your browser
- Select symptoms from the sidebar
- Click "Predict Disease"
- View:
- Most likely disease
- Top 3 predictions with confidence
- Disease description & precautions
- Check sidebar for model performance metrics

---

### 🏗️ Project Architecture

disease_prediction_project/
│
├── app.py                  # Streamlit interface
├── train_model.py          # Model training script
├── dataset/
│   └── Training.csv        # Dataset
├── model/
│   └── rf_model.pkl        # Trained model
├── data/
│   └── disease_info.json   # Disease info & precautions
├── metrics/
│   └── model_metrics.json  # Evaluation metrics
└── requirements.txt        # Dependencies

---

### 🔮 Future Work
- Add NLP-based symptom input (text-based detection)
- Use real medical datasets for better accuracy
- Deploy as a mobile or cloud application
- Integrate doctor/hospital recommendations
- Explore deep learning models

---


### ⚠️ Disclaimer

- This AI system is for educational purposes only.
- It does not replace professional medical advice.
- Always consult a licensed doctor for diagnosis or treatment.

--- 

### 📚 References

- Scikit-learn Documentation
- Streamlit Documentation
- Healthcare AI research papers

---
