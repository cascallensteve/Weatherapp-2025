import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(data):
    encoder = LabelEncoder()
    data["weather_condition"] = encoder.fit_transform(data["weather_condition"])
    return data
