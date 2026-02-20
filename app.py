import os
import numpy as np
import cv2
import tensorflow as tf
from flask import Flask, render_template, request

# Create Flask app FIRST
app = Flask(__name__)

os.makedirs("static/uploads", exist_ok=True)

# Load model
model = tf.keras.models.load_model("models/classification_model.keras", compile=False)

IMG_SIZE = 224

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Route AFTER app is defined
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    image_file = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join("static/uploads", file.filename)
            file.save(filepath)

            image_file = file.filename

            img = preprocess_image(filepath)
            pred = model.predict(img)[0][0]

            if pred > 0.5:
                prediction = "Malignant (Cancer)"
                confidence = round(float(pred), 3)
            else:
                prediction = "Benign (Non-Cancer)"
                confidence = round(float(1 - pred), 3)

    return render_template("index.html",
                           prediction=prediction,
                           confidence=confidence,
                           image_file=image_file)

if __name__ == "__main__":
    app.run()