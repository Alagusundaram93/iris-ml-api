from pathlib import Path
import joblib
MODEL_PATH = Path(__file__).resolve().parent / "saved_model" / "model.joblib"

# Load the saved model
model = joblib.load(MODEL_PATH)

# One new Iris flower
sample = [[5.0, 4.0, 6.2, 1.8]]  # Example features for a new Iris flower

# Make prediction
prediction = int(model.predict(sample)[0])

# Convert class number to species name
names = ["setosa", "versicolor", "virginica"]

print("Prediction:", names[prediction])