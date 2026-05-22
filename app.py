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
    version="1.0.1",
    swagger_ui_parameters={
        "syntaxHighlight.theme": "obsidian"
    }
)

# Home route
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <html>
        <head>
            <title>OptiRoute AI Logistics Intelligence</title>

            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #0f172a;
                    color: white;
                    text-align: center;
                    padding-top: 80px;
                }

                h1 {
                    font-size: 48px;
                    color: #38bdf8;
                }

                p {
                    font-size: 20px;
                    width: 70%;
                    margin: auto;
                    line-height: 1.6;
                }

                .button {
                    display: inline-block;
                    margin-top: 30px;
                    padding: 15px 30px;
                    font-size: 18px;
                    color: white;
                    background-color: #2563eb;
                    text-decoration: none;
                    border-radius: 10px;
                    margin-right: 10px;
                }

                .button:hover {
                    background-color: #1d4ed8;
                }

                .features {
                    margin-top: 40px;
                    font-size: 18px;
                }
            </style>
        </head>

        <body>

            <h1>🚚 OptiRoute AI Logistics Intelligence TEST</h1>

            <p>
                AI-Driven Last-Mile Logistics Intelligence System
                powered by Machine Learning, Risk Analytics,
                and Route Optimization.
            </p>

            <div class="features">
                ✅ Delivery Delay Prediction <br><br>
                ✅ Risk-Aware Analytics <br><br>
                ✅ Route Optimization <br><br>
                ✅ FastAPI Cloud Deployment
            </div>

            <a class="button" href="/docs">
                Open API Docs
            </a>

            <a class="button" href="/risk-analytics">
                View Risk Analytics
            </a>

        </body>
    </html>
    """

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

@app.get("/risk-analytics")
def risk_analytics():

    return {
        "high_risk_routes": 18,
        "medium_risk_routes": 42,
        "low_risk_routes": 76,
        "average_delay_probability": 0.27,
        "system_status": "Operational"
    }