from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# Location where the trained model will be saved
MODEL_PATH = Path(__file__).resolve().parent / "saved_model" / "model.joblib"


def train():
    # 1. Load the Iris dataset
    iris = load_iris()

    # 2. Separate input features and target
    X = iris.data
    y = iris.target

    # 3. Split the dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # 4. Create the Machine Learning model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # 5. Train the model
    model.fit(X_train, y_train)

    # 6. Make predictions on test data
    predictions = model.predict(X_test)

    # 7. Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    print(f"Test accuracy: {accuracy:.2%}")

    # 8. Create saved_model folder if it doesn't exist
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    # 9. Save the trained model
    joblib.dump(model, MODEL_PATH)

    print(f"Saved model to: {MODEL_PATH}")


if __name__ == "__main__":
    train()