# Iris Flower Classification ML API

## 1. Project Overview

This project is a Machine Learning REST API that predicts the species of an Iris flower based on its measurements.

The API will receive flower measurements as input and use a trained Machine Learning model to predict the Iris flower species.

The main purpose of this project is to learn how to build and serve a Machine Learning model through a REST API.

---

## 2. Dataset

We will use the Iris dataset provided by scikit-learn.

The dataset contains four measurements for each flower:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The flower can belong to one of three species:

* Setosa
* Versicolor
* Virginica

---

## 3. Machine Learning Problem

The Machine Learning problem is **Classification**.

The model will take the four flower measurements as input and predict which Iris species the flower belongs to.

Example:

```text
Flower Measurements
        ↓
   ML Model
        ↓
     Setosa
```

---

## 4. API Contract

The `/predict` endpoint will accept four numerical values: sepal length, sepal width, petal length, and petal width. The API will validate these values and send them to the trained Machine Learning model. The model will predict the Iris flower species, and the API will return the prediction as a JSON response.

### Input

The API will receive:

* sepal_length
* sepal_width
* petal_length
* petal_width

Example:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Output

The API will return the predicted flower species.

Example:

```json
{
  "prediction": "setosa"
}
```

---

## 5. API Flow

The request will flow through the following steps:

```text
Client
   ↓
POST /predict
   ↓
Input Validation
   ↓
Machine Learning Model
   ↓
Prediction
   ↓
JSON Response
```

### Explanation

1. The client sends flower measurements to `/predict`.
2. The API validates the input.
3. The validated input is sent to the Machine Learning model.
4. The model predicts the Iris species.
5. The API returns the prediction as JSON.

---

## 6. Model vs Service

### Model

The Machine Learning model is responsible for making the prediction.

```text
Input
  ↓
ML Model
  ↓
Prediction
```

### Service

The API service receives requests from clients, validates the input, sends the data to the Machine Learning model, and returns the prediction.

```text
Client
  ↓
FastAPI Service
  ↓
Validation
  ↓
ML Model
  ↓
Response
```

---

## 7. MVP Scope

The first version of this project will contain only the basic functionality required to serve an Iris classification model through an API.

### Included

* Iris dataset
* Machine Learning classification model
* Model training
* Model evaluation
* Saved Machine Learning model
* FastAPI application
* `/predict` endpoint
* Input validation
* JSON prediction response

### Not Included

* Login
* Signup
* Database
* Frontend
* Admin dashboard
* Multiple models
* Multiple datasets

The goal is to keep the project simple and focus on Machine Learning API engineering.

---

## 8. Project Plan

### Task 1

Plan the project and API architecture.

### Task 2

Create the Python environment and project folder structure.

### Task 3

Train and save the Machine Learning model.

### Task 4

Create the FastAPI application and test the API.

### Future

Connect the saved Machine Learning model to the `/predict` endpoint.

---

## 9. Final Goal

The final application will allow a client to send Iris flower measurements to the `/predict` API and receive the predicted Iris flower species as a JSON response.
