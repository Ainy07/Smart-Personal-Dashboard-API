# 🚀 Smart-Personal-Dashboard-API

An advanced **FastAPI-based personal productivity and analytics system**, combining **Expenses, Weather, News, Sentiment, Notifications, Calendar, Contact, and Admin** — all powered by secure **JWT Authentication**.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?logo=fastapi)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-orange.svg)
[![Docs](https://img.shields.io/badge/API%20Docs-Swagger%20UI-blue)](http://127.0.0.1:8000/docs)
[![ReDoc](https://img.shields.io/badge/API%20Docs-ReDoc-red)](http://127.0.0.1:8000/redoc)

---

## ✨ Features

✅ **JWT Authentication** — secure token-based login  
💰 **Expense Tracker** — add, view, and analyze spending  
📊 **Expense Summary & Trends** — total and category-wise insights  
🌦️ **Weather API** — real-time weather data  
📰 **News API** — trending news headlines  
💬 **Sentiment Analysis** — analyze tone using TextBlob  
🔔 **Notifications** — reminders + email alerts  
📅 **Calendar API** — weekly summary view  
💌 **Contact Form** — collect feedback  
👩‍💼 **Admin Dashboard** — manage users & feedback  
⚙️ **Rate Limiting** — protect API with slowapi  

---

## 🧰 Tech Stack

| Category | Tools |
|-----------|-------|
| **Framework** | FastAPI |
| **Database ORM** | SQLAlchemy |
| **Database** | SQLite (default) |
| **Authentication** | JWT (`python-jose`), Passlib |
| **Scheduler** | APScheduler |
| **Email Sending** | smtplib + Gmail App Password |
| **Rate Limiter** | SlowAPI |
| **Environment Vars** | python-dotenv |
| **Testing** | Postman / Thunder Client / Swagger Docs |
| **Deployment** | Render / Railway / Localhost |

---
smart_dashboard/  
│
├── app/                            
│   ├── main.py                   
│   ├── database.py               
│   ├── models.py                 
│   ├── utils/                    
│   │   ├── jwt_handler.py       
│   │   ├── dependencies.py        
│   ├── routes/                   
│   │   ├── auth_routes.py        
│   │   ├── expense.py           
│   │   ├── weather.py          
│   │   ├── news.py               
│   │   ├── sentiment.py         
│   ├── routers/                  
│   │   ├── notifications.py      
│   │   ├── calendar_api.py       
│   │   ├── contact.py           
│   │   ├── admin.py              
│   └── init.py           
│
├── dashboard.db                 
├── .env                          
├── requirements.txt            
└── README.md                    


### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ainy07/Smart-Personal-Dashboard-API.git  
cd Smart-Personal-Dashboard-API
```
```
Windows:

python -m venv venv  
venv\Scripts\activate
```

```
Mac/Linux:

python3 -m venv venv  
source venv/bin/activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Create .env File
Create a .env file in the project root with:
SECRET_KEY=your_secret_key  
ALGORITHM=HS256  
ACCESS_TOKEN_EXPIRE_MINUTES=60  
EMAIL_USER=yourapp@gmail.com  
EMAIL_PASS=your_app_password  
WEATHER_API_KEY=your_weather_api_key  
NEWS_API_KEY=your_news_api_key  


Replace placeholders with actual values (e.g., Gmail App Password, API keys from OpenWeatherMap, NewsAPI).

### Requirements
plaintextfastapi==0.111.0  
uvicorn  
sqlalchemy  
passlib[argon2]  
python-jose  
python-dotenv  
textblob  
apscheduler  
slowapi  
requests  
pandas  
matplotlib  
### Install manually if needed:
pip install fastapi==0.111.0 uvicorn sqlalchemy passlib[argon2] python-jose python-dotenv textblob apscheduler slowapi requests pandas matplotlib
### API Endpoints

| Module            | Method | Endpoint               | Description             |
| ----------------- | ------ | ---------------------- | ----------------------- |
| **Auth**          | POST   | `/auth/register`       | Register user           |
|                   | POST   | `/auth/login`          | Login user              |
|                   | GET    | `/auth/me`             | Get current user        |
| **Expenses**      | GET    | `/expenses/`           | Get all expenses        |
|                   | POST   | `/expenses/`           | Add new expense         |
|                   | GET    | `/expenses/summary`    | Expense summary         |
|                   | GET    | `/expenses/trends`     | Monthly trend           |
| **Weather**       | GET    | `/weather/{city}`      | Get live weather        |
| **News**          | GET    | `/news/{country}`      | Latest news             |
| **Sentiment**     | POST   | `/sentiment/`          | Analyze text            |
| **Notifications** | GET    | `/notifications/`      | Check reminders         |
|                   | POST   | `/notifications/email` | Send email notification |
| **Calendar**      | GET    | `/calendar/week`       | Weekly overview         |
| **Contact**       | POST   | `/contact/`            | Submit feedback         |
| **Admin**         | GET    | `/admin/users`         | View all users          |
|                   | DELETE | `/admin/users/{id}`    | Delete user             |
| **System**        | GET    | `/`                    | Welcome message         |
|                   | GET    | `/ping`                | Health check            |

### Authentication & Authorization
Register at /auth/register.  
Login at /auth/login to get an access_token.  
In Swagger UI, click Authorize and paste Bearer <token>.  
Access protected endpoints.  

### Modules Overview

🔐 Auth System: JWT-based login/register with Argon2 hashing and token expiration.  
💰 Expense Analytics: Add/view expenses, view summaries, and monthly trends.  
🌦 Weather + 📰 News: Fetch real-time data using external APIs.  
💬 Sentiment: Analyze text tone with TextBlob.  
🔔 Notifications: Manage reminders and send email alerts.  
📅 Calendar: Weekly expense summary view.  
💌 Contact: Submit feedback via API.  
👩‍💼 Admin: Manage users and feedback messages.  

### Run the Project
```
Option 1 — Using Uvicorn
uvicorn app.main:app --reload
Option 2 — Using Python
python -m uvicorn app.main:app --reload
```
### Open your browser:

👉 http://127.0.0.1:8000/docs (Swagger UI)  
👉 http://127.0.0.1:8000/redoc (ReDoc UI)

### Test Your APIs

✅ Swagger UI: Interactive API docs at /docs.  
⚡ Thunder Client (VS Code): Simple local testing.  
🧰 Postman: Set Authorization: Bearer <token> for secured routes.

Author
Ainy Gupta
Python | FastAPI | Django | ML | Analytics

📧 Email: ainygupta00@gmail.com  
🌐 GitHub: github.com/ainy07  
💼 LinkedIn: www.linkedin.com/in/ainy-gupta-882917242
