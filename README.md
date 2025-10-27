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
├── app/                        # Core application directory
│   ├── main.py                 # Application entry point
│   ├── database.py             # Database configuration and setup
│   ├── models.py               # SQLAlchemy models and schemas
│   ├── utils/                  # Utility modules
│   │   ├── jwt_handler.py      # JWT authentication and token handling
│   │   ├── dependencies.py     # Shared dependencies and helpers
│   ├── routes/                 # API route definitions
│   │   ├── auth_routes.py      # Authentication endpoints
│   │   ├── expense.py          # Expense management endpoints
│   │   ├── weather.py          # Weather data endpoints
│   │   ├── news.py             # News feed endpoints
│   │   ├── sentiment.py        # Sentiment analysis endpoints
│   ├── routers/                # Additional feature routers
│   │   ├── notifications.py    # Notification endpoints
│   │   ├── calendar_api.py     # Calendar integration endpoints
│   │   ├── contact.py          # Contact management endpoints
│   │   ├── admin.py            # Admin-specific endpoints
│   └── init.py             # Package initializer
│
├── dashboard.db                # SQLite database file
├── .env                        # Environment variables
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
text## Installation Guide

### Clone the Repository
```bash
git clone https://github.com/ainy07/Smart-Personal-Dashboard-API.git
cd Smart-Personal-Dashboard-API
Create Virtual Environment

Windows:

bashpython -m venv venv
venv\Scripts\activate

Mac/Linux:

bashpython3 -m venv venv
source venv/bin/activate
Install Dependencies
bashpip install -r requirements.txt
Create .env File
Create a .env file in the project root with:
plaintextSECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
EMAIL_USER=yourapp@gmail.com
EMAIL_PASS=your_app_password
WEATHER_API_KEY=your_weather_api_key
NEWS_API_KEY=your_news_api_key

Replace placeholders with actual values (e.g., Gmail App Password, API keys from OpenWeatherMap, NewsAPI).

Requirements
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
Install manually if needed:
bashpip install fastapi==0.111.0 uvicorn sqlalchemy passlib[argon2] python-jose python-dotenv textblob apscheduler slowapi requests pandas matplotlib
API Endpoints

ModuleMethodEndpointDescriptionAuthPOST/auth/registerRegister userPOST/auth/loginLogin userGET/auth/meGet current userExpensesGET/expenses/Get all expensesPOST/expenses/Add new expenseGET/expenses/summaryExpense summaryGET/expenses/trendsMonthly trendWeatherGET/weather/{city}Get live weatherNewsGET/news/{country}Latest newsSentimentPOST/sentiment/Analyze textNotificationsGET/notifications/Check remindersPOST/notifications/emailSend email notificationCalendarGET/calendar/weekWeekly overviewContactPOST/contact/Submit feedbackAdminGET/admin/usersView all usersDELETE/admin/users/{id}Delete userSystemGET/Welcome messageGET/pingHealth check
Authentication & Authorization

Register at /auth/register.
Login at /auth/login to get an access_token.
In Swagger UI, click Authorize and paste Bearer <token>.
Access protected endpoints.

Modules Overview

🔐 Auth System: JWT-based login/register with Argon2 hashing and token expiration.
💰 Expense Analytics: Add/view expenses, view summaries, and monthly trends.
🌦 Weather + 📰 News: Fetch real-time data using external APIs.
💬 Sentiment: Analyze text tone with TextBlob.
🔔 Notifications: Manage reminders and send email alerts.
📅 Calendar: Weekly expense summary view.
💌 Contact: Submit feedback via API.
👩‍💼 Admin: Manage users and feedback messages.

Run the Project
Option 1 — Using Uvicorn
bashuvicorn app.main:app --reload
Option 2 — Using Python
bashpython -m uvicorn app.main:app --reload
Open your browser:

👉 http://127.0.0.1:8000/docs (Swagger UI)
👉 http://127.0.0.1:8000/redoc (ReDoc UI)

Test Your APIs

✅ Swagger UI: Interactive API docs at /docs.
⚡ Thunder Client (VS Code): Simple local testing.
🧰 Postman: Set Authorization: Bearer <token> for secured routes.

Deployment
Render or Railway

Push the repo to GitHub.
Create a new Web Service on Render/Railway.
Set:

Build Command: pip install -r requirements.txt
Start Command: uvicorn app.main:app --host 0.0.0.0 --port 10000


Add .env variables in the platform's dashboard.
Deploy 🎉

Future Enhancements

🔔 Push notifications (Firebase)
📈 AI-powered expense prediction
💳 Wallet / UPI integration
📤 Export analytics as PDF/Excel
🌐 React-based frontend dashboard

Screenshots (Optional)

Swagger UI (/docs)
Expense Summary response
Notification logs
Calendar weekly view

License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.
Author
Ainy Gupta
Python | FastAPI | Django | ML | Analytics

📧 Email: ainygupta00@gmail.com
🌐 GitHub: github.com/ainy07
💼 LinkedIn: linkedin.com/in/ainy-gupta

Contributions

Contributions are welcome!
Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.
