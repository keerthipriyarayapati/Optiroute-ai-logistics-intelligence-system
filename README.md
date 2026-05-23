# OptiRoute — AI-Driven Last-Mile Logistics Intelligence System

OptiRoute is an AI-powered logistics intelligence platform designed to predict delivery delays, analyze shipment risks, and support last-mile delivery optimization using Machine Learning, predictive analytics, and FastAPI cloud deployment.

The platform combines predictive analytics, logistics intelligence, and cloud-hosted APIs to provide efficient and data-driven delivery management solutions.

## Live Deployment

Main Platform:  
https://optiroute-ai-logistics-intelligence.onrender.com

API Documentation:  
https://optiroute-ai-logistics-intelligence.onrender.com/docs

---

## Features

- Delivery Delay Prediction using Machine Learning
- Risk-Aware Logistics Analytics
- Last-Mile Logistics Intelligence
- Cloud-Hosted FastAPI Deployment
- Interactive API Documentation
- Real-Time Prediction Engine
- Professional Web-Based Interface

---

## Technology Stack

- Python
- FastAPI
- Scikit-learn
- NumPy
- Joblib
- Uvicorn
- Render
- HTML/CSS

---

## Installation

Clone the repository:

```bash
git clone https://github.com/keerthipriyarayapati/Optiroute-ai-logistics-intelligence-system.git
````

Navigate to the project directory:

```bash
cd Optiroute-ai-logistics-intelligence-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn app:app --reload
```

---

## API Endpoints

| Endpoint           | Method | Description                   |
| ------------------ | ------ | ----------------------------- |
| `/`                | GET    | Main Platform Interface       |
| `/docs`            | GET    | Swagger API Documentation     |
| `/predict-delay`   | POST   | Delivery Delay Prediction API |
| `/website-predict` | POST   | Web Prediction Interface      |
| `/risk-analytics`  | GET    | Risk Analytics API            |

---

## Example Prediction Request

```json
{
  "price": 120,
  "freight_value": 25,
  "purchase_hour": 18,
  "purchase_day": 12,
  "purchase_month": 7,
  "purchase_weekday": 2,
  "is_weekend": 0,
  "delivery_time_days": 10
}
```

---

## Example Prediction Response

```json
{
  "delivery_delay_prediction": 0,
  "delay_probability": 0.18
}
```

---

## Machine Learning Workflow

1. Data Preprocessing
2. Feature Engineering
3. Model Training
4. Delivery Delay Prediction
5. Risk Classification
6. API Deployment
7. Cloud Hosting

---

## Project Highlights

* Developed an end-to-end AI logistics intelligence platform
* Built a cloud-hosted Machine Learning prediction API
* Implemented delivery delay prediction using predictive analytics
* Designed a FastAPI-powered logistics intelligence system
* Integrated deployment-ready API infrastructure using Render
