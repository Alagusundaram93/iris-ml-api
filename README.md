# Iris ML API

## 1. Project Overview

Iris ML API is a simple Machine Learning REST API that predicts the species of an iris flower based on its physical measurements. The project uses the Iris dataset and a classification model from scikit-learn. The main goal of this project is to learn how to train a Machine Learning model and serve that model through a clean FastAPI service.

## 2. Problem Statement

The problem is to classify an iris flower into one of three species based on four measurements:

* Sepal length
* Sepal width
* Petal length
* Petal width

The three possible classes are:

* Setosa
* Versicolor
* Virginica

## 3. Dataset

This project uses the built-in Iris dataset provided by scikit-learn.

The dataset contains 150 samples with four input features:

* Sepal length
* Sepal width
* Petal length
* Petal width

The target variable is the iris flower species.

## 4. Machine Learning Problem

This is a supervised Machine Learning classification problem.

The model will learn the relationship between the four flower measurements and the corresponding iris species.

For the initial version of this project, a simple classification model such as Logistic Regression will be used.

## 5. API Contract

The API will provide a `POST /predict` endpoint.

The endpoint accepts four numerical flower measurements:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

The API validates the input and sends the valid measurements to the trained Machine Learning model.

The model predicts the iris species and the API returns the prediction as JSON.

Example response:

```json
{
  "prediction": "setosa"
}
```

## 6. Request → Validation → Model → Response Flow

```text
Client
   ↓
POST /predict
   ↓
Validate input
   ↓
Send validated features to ML model
   ↓
Model predicts iris species
   ↓
Return prediction as JSON response
```

## 7. MVP Scope

The first version of the project will keep the scope small.

The MVP will include:

* Iris dataset
* One Machine Learning classification model
* Model training
* Saving the trained model
* FastAPI application
* `/predict` endpoint
* Input validation
* Prediction response
* Basic tests

The project will not include authentication, databases, frontend applications, or complex Machine Learning techniques in the initial version.

## 8. Planned Technology Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
* scikit-learn
* pandas
* pytest
* Git and GitHub

## 9. Project Goal

The main goal is to understand how a Machine Learning model becomes a usable API service.

The project will demonstrate the complete flow:

```text
Dataset
   ↓
Train Model
   ↓
Save Model
   ↓
Load Model
   ↓
FastAPI
   ↓
Validate Request
   ↓
Predict
   ↓
Return Response
```