from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Initialize app
app = FastAPI(
    title="OptiRoute AI Logistics Intelligence API",
    description="AI-Driven Last-Mile Logistics Intelligence System",
    version="2.0.0"
)

# HOME PAGE
@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <html>

    <head>
        <title>OptiRoute AI</title>

        <style>

            body{
                margin:0;
                padding:0;
                font-family:Arial;
                background:#071133;
                color:white;
                text-align:center;
            }

            .hero{
                padding-top:100px;
            }

            h1{
                font-size:60px;
                margin-bottom:20px;
            }

            p{
                font-size:22px;
                color:#d1d5db;
            }

            .form-box{
                margin-top:50px;
            }

            input{
                width:220px;
                padding:15px;
                margin:10px;
                border:none;
                border-radius:10px;
                font-size:16px;
            }

            button{
                padding:15px 40px;
                border:none;
                border-radius:10px;
                background:#2563eb;
                color:white;
                font-size:18px;
                cursor:pointer;
                margin-top:20px;
            }

            button:hover{
                background:#1d4ed8;
            }

            .cards{
                display:flex;
                justify-content:center;
                gap:30px;
                margin-top:100px;
                flex-wrap:wrap;
            }

            .card{
                width:250px;
                background:#172554;
                padding:40px;
                border-radius:20px;
                box-shadow:0px 4px 20px rgba(0,0,0,0.3);
            }

            .card h2{
                font-size:45px;
                color:#38bdf8;
            }

            .footer{
                margin-top:100px;
                padding-bottom:40px;
                color:#94a3b8;
            }

        </style>

    </head>

    <body>

        <div class="hero">

            <h1>🚚 OptiRoute AI</h1>

            <p>
                AI-Driven Last-Mile Logistics Intelligence System
            </p>

            <div class="form-box">

                <form action="/predict-delay" method="post">

                    <input type="number" step="any" name="price"
                    placeholder="Product Price" required>

                    <input type="number" step="any" name="freight_value"
                    placeholder="Freight Value" required>

                    <input type="number" step="any" name="delivery_time_days"
                    placeholder="Delivery Time Days" required>

                    <br>

                    <button type="submit">
                        Predict Delivery Risk
                    </button>

                </form>

            </div>

            <div class="cards">

                <div class="card" style="border-top:5px solid #ef4444;">
                    <h2>ML</h2>
                    <p>Prediction Engine</p>
                </div>

                <div class="card" style="border-top:5px solid #f59e0b;">
                    <h2>AI</h2>
                    <p>Risk Analytics</p>
                </div>

                <div class="card" style="border-top:5px solid #22c55e;">
                    <h2>API</h2>
                    <p>Cloud Deployment</p>
                </div>

            </div>

            <div class="footer">
                OptiRoute AI Logistics Intelligence System © 2026
            </div>

        </div>

    </body>

    </html>
    """

# PREDICTION PAGE
@app.post("/predict-delay", response_class=HTMLResponse)
def predict_delay(

    price: float = Form(...),
    freight_value: float = Form(...),
    delivery_time_days: float = Form(...)

):

    # Dummy values for remaining features
    purchase_hour = 12
    purchase_day = 15
    purchase_month = 7
    purchase_weekday = 2
    is_weekend = 0

    features = np.array([[
        price,
        freight_value,
        purchase_hour,
        purchase_day,
        purchase_month,
        purchase_weekday,
        is_weekend,
        delivery_time_days
    ]])

    prediction = int(model.predict(features)[0])

    probability = float(model.predict_proba(features)[0][1])

    # Risk label
    if probability > 0.7:
        risk = "HIGH RISK"
        color = "#ef4444"

    elif probability > 0.4:
        risk = "MEDIUM RISK"
        color = "#f59e0b"

    else:
        risk = "LOW RISK"
        color = "#22c55e"

    return f"""

    <html>

    <head>

        <title>Prediction Result</title>

        <style>

            body{{
                font-family:Arial;
                background:#071133;
                color:white;
                text-align:center;
                padding-top:100px;
            }}

            .card{{
                width:500px;
                margin:auto;
                background:#172554;
                padding:50px;
                border-radius:20px;
                border-top:10px solid {color};
            }}

            h1{{
                font-size:50px;
            }}

            h2{{
                font-size:40px;
                color:{color};
            }}

            p{{
                font-size:24px;
            }}

            a{{
                display:inline-block;
                margin-top:30px;
                padding:15px 30px;
                background:#2563eb;
                color:white;
                text-decoration:none;
                border-radius:10px;
            }}

        </style>

    </head>

    <body>

        <div class="card">

            <h1>Prediction Result</h1>

            <h2>{risk}</h2>

            <p>
                Delay Prediction:
                <b>{prediction}</b>
            </p>

            <p>
                Delay Probability:
                <b>{round(probability * 100, 2)}%</b>
            </p>

            <a href="/">
                Back to Home
            </a>

        </div>

    </body>

    </html>
    """

# RISK ANALYTICS API
@app.get("/risk-analytics")
def risk_analytics():

    return {
        "high_risk_routes": 18,
        "medium_risk_routes": 42,
        "low_risk_routes": 76,
        "average_delay_probability": 0.27,
        "system_status": "Operational"
    }