from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app import models, database
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/calendar", tags=["Calendar"])

@router.get("/weekly")
def weekly_expense_summary(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    today = datetime.utcnow()
    week_start = today - timedelta(days=7)
    expenses = (
        db.query(models.Expense)
        .filter(models.Expense.owner_id == current_user.id, models.Expense.created_at >= week_start)
        .all()
    )

    total = sum(e.amount for e in expenses)
    return {
        "week_start": week_start.date(),
        "week_end": today.date(),
        "total_expenses": total,
        "count": len(expenses),
    }
