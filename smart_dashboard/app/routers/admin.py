from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app import models
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users
@router.get("/expenses")
def get_all_expenses(db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).all()
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found")
    return expenses