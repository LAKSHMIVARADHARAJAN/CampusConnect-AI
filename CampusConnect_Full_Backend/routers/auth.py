#auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Staff
from utils.security import verify_password, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(unique_id: str, password: str, db: Session = Depends(get_db)):
    user = db.query(Staff).filter(Staff.unique_id == unique_id).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": user.unique_id,
        "role": user.role
    })

    return {"access_token": token, "token_type": "bearer"}
