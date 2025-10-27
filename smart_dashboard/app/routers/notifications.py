from fastapi import APIRouter, Depends, BackgroundTasks
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from app.database import get_db
from app import models

router = APIRouter()
scheduler = BackgroundScheduler()



def send_email_notification(to_email: str, subject: str, body: str):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = "ainygupta00@gmail.com"
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("ainygupta00@gmail.com", "fnrc dcdk sgry mpzj") 
            server.send_message(msg)

        print(f"📧 Email sent to {to_email}")

    except Exception as e:
        print(f"❌ Email sending failed: {e}")


def send_daily_reminder(db: Session):
    message = "This is your daily reminder! 💡 Don't forget to check your dashboard."
    reminder = models.Notification(message=message, timestamp=datetime.now())
    db.add(reminder)
    db.commit()


    send_email_notification("user@example.com", "Daily Reminder", message)

    print(f"[{datetime.now()}] 🔔 Reminder sent and saved to DB.")


def start_scheduler():
    """Ensures scheduler starts only once."""
    if not scheduler.running:
        scheduler.start()
        print("✅ Notification scheduler started.")


def schedule_daily_job():
    scheduler.add_job(
        lambda: send_daily_reminder(next(get_db())),
        "interval",
        hours=24,
        id="daily_reminder",
        replace_existing=True
    )

schedule_daily_job()
start_scheduler()


@router.get("/")
def get_notifications_status():
    """Check scheduler status"""
    return {"message": "🔔 Daily notifications are active and running!"}


@router.get("/all")
def get_all_notifications(db: Session = Depends(get_db)):
    """View all saved notifications"""
    return db.query(models.Notification).order_by(models.Notification.timestamp.desc()).all()


@router.post("/set-reminder")
def set_reminder(hour: int, minute: int):
    """Set user-customized reminder time"""
    job_id = f"user_reminder_{hour}_{minute}"
    scheduler.add_job(
        lambda: send_daily_reminder(next(get_db())),
        "cron",
        hour=hour,
        minute=minute,
        id=job_id,
        replace_existing=True
    )
    return {"message": f"🕒 Reminder set for {hour:02d}:{minute:02d} daily!"}


@router.post("/send-test-email")
def send_test_email(background_tasks: BackgroundTasks, to_email: str):
    """Send a test email notification"""
    background_tasks.add_task(
        send_email_notification,
        to_email,
        "Test Notification",
        "✅ Your Smart Dashboard email system is working!"
    )
    return {"message": f"Test email scheduled to {to_email}"}


@router.get("/push")
def simulate_push_notification():
    """Simulate a push notification (frontend or WebSocket integration point)"""
    return {"message": "📱 Push notification sent (simulation)"}
