from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import pandas as pd

from app import models, schemas, database
from app.utils.dependencies import get_current_user  

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("/")
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_expense = models.Expense(
        **expense.dict(),
        owner_id=current_user.id,
        created_at=datetime.utcnow()
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return {"message": "Expense added successfully", "expense": new_expense.id}


@router.get("/")
def get_expenses(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    expenses = db.query(models.Expense).filter(models.Expense.owner_id == current_user.id).all()
    return expenses


@router.get("/summary")
def get_expense_summary(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    expenses = db.query(models.Expense).filter(models.Expense.owner_id == current_user.id).all()
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found")

    df = pd.DataFrame([{"amount": e.amount, "category": e.category} for e in expenses])
    total_spent = df["amount"].sum()
    avg_spent = df["amount"].mean()
    category_wise = df.groupby("category")["amount"].sum().to_dict()

    return {
        "total_spent": round(total_spent, 2),
        "average_spent": round(avg_spent, 2),
        "category_wise": category_wise
    }


@router.get("/trends")
def get_expense_trends(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    expenses = db.query(models.Expense).filter(models.Expense.owner_id == current_user.id).all()
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found")

    df = pd.DataFrame([
        {"amount": e.amount, "month": e.created_at.strftime("%Y-%m")}
        for e in expenses
    ])
    trends = df.groupby("month")["amount"].sum().reset_index().to_dict(orient="records")

    return {"monthly_trend": trends}
