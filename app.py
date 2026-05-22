from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Initialize FastAPI app
app = FastAPI(
    title="OptiRoute AI Logistics Intelligence API",
    description="""
🚚 AI-Driven Last-Mile Logistics Intelligence System

Features:
- Delivery Delay Prediction
- Risk-Aware Analytics
- Route Optimization
- Logistics Intelligence API
""",
    version="1.0.0",
    swagger_ui_parameters={
        "syntaxHighlight.theme": "obsidian"
    }
)

# Home route
@app.get("/")
def home():
    return {
        "message": "OptiRoute Logistics API Running Successfully"
    }

# Input schema
class DeliveryInput(BaseModel):
    price: float
    freight_value: float
    purchase_hour: int
    purchase_day: int
    purchase_month: int
    purchase_weekday: int
    is_weekend: int
    delivery_time_days: float

# Prediction endpoint
@app.post("/predict-delay")
def predict_delay(data: DeliveryInput):

    features = np.array([[
        data.price,
        data.freight_value,
        data.purchase_hour,
        data.purchase_day,
        data.purchase_month,
        data.purchase_weekday,
        data.is_weekend,
        data.delivery_time_days
    ]])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    return {
        "delivery_delay_prediction": int(prediction),
        "delay_probability": float(probability)
    }