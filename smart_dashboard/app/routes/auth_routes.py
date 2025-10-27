from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from pydantic import BaseModel, constr

from app.utils.dependencies import get_current_user
from app.utils.jwt_handler import create_access_token
from .. import models
from ..database import get_db

router = APIRouter()
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: constr(min_length=6, max_length=72)   # type: ignore

class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    existing_email = db.query(models.User).filter(models.User.email == request.email).first()
    existing_username = db.query(models.User).filter(models.User.username == request.username).first()

    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = pwd_context.hash(request.password)
    new_user = models.User(
        username=request.username,
        email=request.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }



@router.post("/login")
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not pwd_context.verify(request.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    access_token = create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username
    }



@router.get("/me")
def get_user_data(current_user: models.User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "email": current_user.email
    }