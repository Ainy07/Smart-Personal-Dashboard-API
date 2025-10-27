from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request
from app.database import Base, engine
from app import models

from app.routers import calendar_api, contact, notifications
from app.routes import auth_routes, expense, weather, news, sentiment
from app.routers import admin

# ✅ Create database tables
models.Base.metadata.create_all(bind=engine)
print("✅ Database tables created successfully!")

app = FastAPI(title="Smart Personal Dashboard API")

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    lambda r, e: JSONResponse(status_code=429, content={"detail": "Too many requests"})
)
app.add_middleware(SlowAPIMiddleware)

# ✅ Include Routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(expense.router, prefix="/expenses", tags=["Expenses"])
app.include_router(weather.router, prefix="/weather", tags=["Weather"])
app.include_router(news.router, prefix="/news", tags=["News"])
app.include_router(sentiment.router, tags=["Sentiment"])

app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(calendar_api.router, prefix="/calendar", tags=["Calendar"])
app.include_router(contact.router, prefix="/contact", tags=["Contact"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def root():
    return {"message": "Welcome to Smart Personal Dashboard API 🚀"}

@app.get("/ping")
@limiter.limit("5/minute")
def ping(request: Request):
    return {"message": "pong"}