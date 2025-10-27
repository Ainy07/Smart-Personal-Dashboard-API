from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app import models, database

router = APIRouter(prefix="/contact", tags=["Contact"])

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

@router.post("/")
def submit_contact(form: ContactForm, db: Session = Depends(database.get_db)):
    contact = models.Contact(**form.dict())
    db.add(contact)
    db.commit()
    return {"message": "Feedback submitted successfully"}
