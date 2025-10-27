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
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── utils/
│ │ ├── jwt_handler.py
│ │ ├── dependencies.py
│ ├── routes/
│ │ ├── auth_routes.py
│ │ ├── expense.py
│ │ ├── weather.py
│ │ ├── news.py
│ │ ├── sentiment.py
│ ├── routers/
│ │ ├── notifications.py
│ │ ├── calendar_api.py
│ │ ├── contact.py
│ │ ├── admin.py
│ └── init.py
│
├── dashboard.db
├── .env
├── requirements.txt
└── README.md


---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ainy07/Smart-Personal-Dashboard-API.git
cd Smart-Personal-Dashboard-API

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


Install manually if needed:

pip install fastapi uvicorn sqlalchemy passlib[argon2] python-jose python-dotenv textblob apscheduler slowapi requests pandas matplotlib

🧾 API Endpoints (All Routes)
Module	Method	Endpoint	Description
Auth	POST	/auth/register	Register user
	POST	/auth/login	Login user
	GET	/auth/me	Get current user
Expenses	GET	/expenses/	Get all expenses
	POST	/expenses/	Add new expense
	GET	/expenses/summary	Expense summary
	GET	/expenses/trends	Monthly trend
Weather	GET	/weather/{city}	Get live weather
News	GET	/news/{country}	Latest news
Sentiment	POST	/sentiment/	Analyze text
Notifications	GET	/notifications/	Check reminders
	POST	/notifications/email	Send email notification
Calendar	GET	/calendar/week	Weekly overview
Contact	POST	/contact/	Submit feedback
Admin	GET	/admin/users	View all users
	DELETE	/admin/users/{id}	Delete user
System	GET	/	Welcome message
	GET	/ping	Health check
🔐 Authentication & Authorization

1️⃣ Register → /auth/register
2️⃣ Login → /auth/login → copy access_token
3️⃣ Go to Swagger → click Authorize → paste Bearer <token>
4️⃣ Access protected endpoints

🧠 Modules Overview
🔐 Auth System

JWT-based login & register

Argon2 password hashing

Auto token expiration

💰 Expense Analytics

Add/view expenses

Summary and monthly trend

🌦 Weather + 📰 News

Fetch real-time info from APIs

💬 Sentiment

Analyze text tone using TextBlob

🔔 Notifications

Store & manage reminders

Send email alerts

📅 Calendar

Get weekly expense summary

💌 Contact

Submit feedback through API

👩‍💼 Admin

Manage users and messages

💻 Run the Project
▶ Option 1 — Using Uvicorn
uvicorn app.main:app --reload

▶ Option 2 — Using Python
python -m uvicorn app.main:app --reload


Now open your browser:
👉 http://127.0.0.1:8000/docs
 (Swagger UI)
👉 http://127.0.0.1:8000/redoc
 (ReDoc UI)

🧪 Test Your APIs

You can test using:

✅ Swagger UI

Auto-generated API docs

Interactive request testing

⚡ Thunder Client (VS Code)

Simple local testing interface

🧰 Postman

Set header Authorization: Bearer <token> for secured routes

🚀 Deployment
🌐 Render or Railway

Push this repo to GitHub

Create a new Web Service

Set:

Build Command: pip install -r requirements.txt

Start Command: uvicorn app.main:app --host 0.0.0.0 --port 10000

Add .env variables in dashboard

Deploy 🎉

🔮 Future Enhancements

🔔 Push notifications (Firebase)

📈 AI-powered expense prediction

💳 Wallet / UPI integration

📤 Export analytics as PDF/Excel

🌐 React-based frontend dashboard

📸 Screenshots (Optional)

Add images like:

/docs Swagger UI

Expense Summary response

Notification logs

Calendar weekly view

📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute.

👩‍💻 Author

Ainy Gupta

Python | FastAPI | Django | ML | Analytics

📧 Email: ainygupta00@gmail.com

🌐 GitHub: github.com/ainy07

💼 LinkedIn: linkedin.com/in/ainy-gupta

## 📂 Project Structure

