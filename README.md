🩺 AI-Powered Skin Cancer Detection System

A Deep Learning-based web application for automated skin cancer classification using MobileNetV2 and Flask.

🚀 Features

Binary classification (Benign / Malignant)

Transfer learning using MobileNetV2

Class imbalance handling

Confidence score display

Modern Bootstrap UI

Flask backend

Deployable on cloud

📊 Model Performance

Accuracy: 85%

Malignant Recall: 85%

Reduced False Negatives

Class-weighted training

🧠 Dataset

HAM10000 Dermoscopic Image Dataset
10,015 images across 7 classes
Converted to binary classification

🏗 Architecture
Upload Image
      ↓
Preprocessing (224x224)
      ↓
MobileNetV2
      ↓
Dense Layers
      ↓
Prediction + Confidence
🛠 Technologies Used

Python

TensorFlow / Keras

OpenCV

Flask

Bootstrap

Gunicorn

Render (Deployment)

⚙ Installation (Local)
git clone <[(https://github.com/atharva-dharankar0007/Skin-Cancer-detection-system-)]>
cd skin-cancer-project
pip install -r requirements.txt
python app.py

Open:

http://127.0.0.1:5000
🌍 Deployment

Deployed using Render with:

web: gunicorn app:app

⚠ Disclaimer

This AI system is for educational and research purposes only.
It is not a substitute for professional medical diagnosis.

👨‍💻 Author

Atharva Dharankar
Final Year Computer Science Engineering Student
