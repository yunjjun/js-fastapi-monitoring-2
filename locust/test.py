import requests
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
        "C:\\mlops\\lectures\\js-fastapi-monitoring-2\\winequality-red.csv",
        delimiter=",",
    )
    .rename(columns=feature_columns)
    .drop("quality", axis=1)
    .to_dict(orient="records")
)

record = random.choice(dataset).copy()
r = requests.post('http://114.203.232.71:5000/predict',data = record)
print(r.text)
