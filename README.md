# 🩺 AI-Powered Skin Cancer Detection System

> A Deep Learning–based web application for automated skin cancer classification using MobileNetV2 (Transfer Learning) and Flask.

---

## 📌 Project Overview

Skin cancer is one of the most common types of cancer worldwide. Early detection significantly improves survival rates.

This project presents a deployable AI-powered web application that classifies dermoscopic skin lesion images as:

- ✅ Benign (Non-Cancer)
- ⚠ Malignant (Cancer)

The system uses Transfer Learning with MobileNetV2 and is deployed using Flask.

---

## 🚀 Key Features

- 🧠 Deep Learning-based image classification
- 🔁 Transfer Learning using MobileNetV2
- ⚖ Class imbalance handling using class weights
- 📊 Confidence score visualization
- 🎨 Modern Bootstrap-based UI
- 🌍 Web deployment ready (Render compatible)
- 📦 Lightweight model (~11MB)

---

## 📊 Model Performance

Confusion Matrix:

[[2057  345]
 [  90  508]]

Evaluation Metrics:

- Accuracy: 85%
- Malignant Recall: 85%
- Reduced False Negatives using class-weighted training

Malignant recall is prioritized to minimize missing cancer cases.

---

## 🧠 Dataset Used

HAM10000 Dermoscopic Image Dataset

- 10,015 dermoscopic images
- 7 lesion categories
- Converted into binary classification

Malignant Classes:
- MEL (Melanoma)
- BCC (Basal Cell Carcinoma)
- AKIEC (Actinic Keratosis)

Benign Classes:
- NV
- BKL
- DF
- VASC

The dataset was imbalanced (4:1 ratio), handled using class weighting.

---

## 🏗 System Architecture

User Upload Image  
        ↓  
Image Preprocessing (224x224, Normalization)  
        ↓  
MobileNetV2 (Pretrained CNN)  
        ↓  
Dense Layers  
        ↓  
Sigmoid Output  
        ↓  
Prediction + Confidence Score  

---

## 🛠 Tech Stack

Backend:
- Python
- Flask
- Gunicorn

Deep Learning:
- TensorFlow
- Keras
- MobileNetV2
- OpenCV
- NumPy

Frontend:
- HTML
- Bootstrap
- CSS

Deployment:
- GitHub
- Render

---

## ⚙ Installation (Run Locally)

1️⃣ Clone the Repository

git clone https://github.com/atharva-dharankar0007/Skin-Cancer-detection-system-.git  
cd Skin-Cancer-detection-system-

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Application

python app.py

Open in browser:

http://127.0.0.1:5000

---

## 🌍 Deployment

Deployed using Render with Gunicorn:

web: gunicorn app:app

---

## 📂 Project Structure

skin-cancer-project/
│
├── app.py
├── models/
│     └── classification_model.keras
├── static/
│     └── uploads/
├── templates/
│     └── index.html
├── requirements.txt
├── Procfile
└── README.md

---

## ⚠ Medical Disclaimer

This system is developed for educational and research purposes only.
It is NOT a substitute for professional medical diagnosis.

Always consult a certified dermatologist.

---

## 👨‍💻 Author

Atharva Dharankar  
Final Year – Computer Science Engineering  
Passionate about AI, Machine Learning 


