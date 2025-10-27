from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str

class Expense(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    created_at: datetime
    class Config:
        orm_mode = True

class ExpenseOut(ExpenseBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True  

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        from_attributes = True
