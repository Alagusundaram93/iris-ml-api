from pathlib import Path

import joblib


MODEL_PATH = Path(__file__).resolve().parent / "saved_model" / "model.joblib"


# Load the saved model
model = joblib.load(MODEL_PATH)


# One new Iris flower
sample = [[5.1, 3.5, 1.4, 0.2]]


# Make prediction
prediction = int(model.predict(sample)[0])


# Convert class number to species name
names = ["setosa", "versicolor", "virginica"]

print("Prediction:", names[prediction])