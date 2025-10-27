# Smart-Personal-Dashboard-API
An advanced FastAPI-based personal productivity and analytics system, combining Expenses, Weather, News, Sentiment, Notifications, Calendar, Contact, and Admin — all powered by secure JWT Authentication.


🧭 Table of Contents

✨ Features

🧰 Tech Stack

📂 Project Structure

⚙️ Installation Guide

📦 Requirements

🧾 API Endpoints (All Routes)

🔐 Authentication & Authorization

🧠 Modules Overview

💻 Run the Project (All Methods)

🧪 Test Your APIs

🚀 Deployment (Render--Railway--Localhost)

🔮 Future Enhancements

📸 Screenshots

📜 License

👩‍💻 Author

✨ Features

✅ JWT Authentication — secure token-based login
💰 Expense Tracker — add, view, and analyze spending
📈 Expense Summary & Trends — category, total, and monthly trends
🌦️ Weather API — real-time weather data via OpenWeatherMap
📰 News API — trending news headlines
💬 Sentiment Analysis — analyze text tone with TextBlob
🔔 Notifications — daily reminders + optional email alerts
📅 Calendar API — weekly task and expense overview
💌 Contact Form — collect user feedback
👩‍💼 Admin Dashboard — manage users & feedback
⚙️ Rate Limiting — control API usage via slowapi

🧰 Tech Stack
Category	Tools
Backend Framework	FastAPI
Database ORM	SQLAlchemy
Database	SQLite (default)
Authentication	JWT (python-jose), Passlib
Scheduler	APScheduler
Email Sending	smtplib + Gmail App Password
Rate Limiter	SlowAPI
Environment Variables	python-dotenv
Visualization (optional)	Matplotlib / Bokeh
Deployment	Render / Railway / Localhost
Testing Tools	Thunder Client / Postman / Swagger Docs
📂 Project Structure
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
│   └── __init__.py
│
├── dashboard.db
├── .env
├── requirements.txt
└── README.md

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/ainy07/smart-dashboard.git
cd smart-dashboard

2️⃣ Create Virtual Environment
On Windows:
python -m venv venv
venv\Scripts\activate

On Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Create .env File
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
EMAIL_USER=yourapp@gmail.com
EMAIL_PASS=your_app_password

📦 Requirements
fastapi
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


Install all at once:

pip install fastapi uvicorn sqlalchemy passlib[argon2] python-jose python-dotenv textblob apscheduler slowapi requests pandas matplotlib

🧾 API Endpoints (All Routes)
Module	Method	Endpoint	Description
🔐 Auth	POST	/auth/register	Register new user
	POST	/auth/login	Login user, get JWT token
	GET	/auth/me	Get logged-in user
💰 Expense	GET	/expenses/	View all expenses
	POST	/expenses/	Add expense
	GET	/expenses/summary	Total, average, category breakdown
	GET	/expenses/trends	Monthly expense trend
🌦 Weather	GET	/weather/{city}	Get live weather info
📰 News	GET	/news/{country}	Latest news
💬 Sentiment	POST	/sentiment/	Analyze text sentiment
🔔 Notifications	GET	/notifications/	Get notification status
	POST	/notifications/email	Send email reminder
📅 Calendar	GET	/calendar/week	Get weekly expense summary
💌 Contact	POST	/contact/	Submit feedback form
👩‍💼 Admin	GET	/admin/users	View users
	DELETE	/admin/users/{id}	Delete user
⚙️ Root	GET	/	Welcome message
🧱 Health	GET	/ping	Ping (rate limited)
🔐 Authentication & Authorization

1️⃣ Register → /auth/register
2️⃣ Login → /auth/login → copy "access_token"
3️⃣ In Swagger UI → click Authorize → paste Bearer <token>
4️⃣ Access /auth/me, /expenses, etc.

🧠 Modules Overview
🔐 Auth System

Argon2 password hashing

JWT via python-jose

Token expires in 60 mins

💰 Expense Analytics

/summary: total, average, category split

/trends: month-wise spending trend

🌦 Weather + 📰 News

Live data using APIs

🔔 Notifications

Daily reminders (APScheduler)

Optional email alerts

📅 Calendar

Weekly overview of expenses

💬 Sentiment

TextBlob-based sentiment detection

💌 Contact

Stores feedback in database

👩‍💼 Admin

Manage users & feedback

⚙️ Rate Limiter

/ping: 5 requests/min (SlowAPI)

💻 Run the Project
▶ Option 1 — VS Code Terminal
uvicorn app.main:app --reload

▶ Option 2 — Python Command
python -m uvicorn app.main:app --reload

▶ Option 3 — Run Script

Windows:

@echo off
uvicorn app.main:app --reload
pause


Mac/Linux:

#!/bin/bash
uvicorn app.main:app --reload

🧪 Test Your APIs
🧠 Swagger UI

👉 http://127.0.0.1:8000/docs

⚡ Thunder Client (VS Code)

Open Thunder Client

Create new request

Set method + endpoint

Add body if required

🧰 Postman

Use Authorization: Bearer <token> header

🚀 Deployment (Render / Railway / Localhost)
🌐 On Render
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 10000


✅ Add .env variables and deploy!

🔮 Future Enhancements

✨ Push notifications via Firebase
📈 AI-powered expense prediction
💳 Payment/Wallet Integration
📤 Export reports as PDF/Excel
🌐 React Dashboard Frontend

📸 Screenshots

Add screenshots of:

Swagger UI

Expense Summary

Sentiment Output

Notifications Log

📜 License

Licensed under MIT License — free to use and modify.

👩‍💻 Author

Ainy Gupta

Python | FastAPI | Django | ML | Analytics

📧 Email: ainygupta00@gmail.com

🌐 GitHub: github.com/ainy07