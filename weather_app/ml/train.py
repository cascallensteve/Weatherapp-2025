import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("C:\Users\Comp science\Downloads\weather.csv")

# Preprocess
X = data[["temperature", "humidity", "weather_condition", "wind_speed"]]
y = data["recommendation"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train ML Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ml/model.pkl")
