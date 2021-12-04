from locust import HttpUser, task
import pandas as pd
import random

feature_columns = {
    "fixed acidity": "fixed_acidity",
    "volatile acidity": "volatile_acidity",
    "citric acid": "citric_acid",
    "residual sugar": "residual_sugar",
    "chlorides": "chlorides",
    "free sulfur dioxide": "free_sulfur_dioxide",
    "total sulfur dioxide": "total_sulfur_dioxide",
    "density": "density",
    "pH": "ph",
    "sulphates": "sulphates",
    "alcohol": "alcohol_pct_vol",
}
dataset = (
    pd.read_csv(
        "winequality-red.csv",
        delimiter=",",
    )
    .rename(columns=feature_columns)
    .drop("quality", axis=1)
    .to_dict(orient="records")
)