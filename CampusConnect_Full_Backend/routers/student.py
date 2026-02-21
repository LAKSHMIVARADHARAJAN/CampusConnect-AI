#student.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Student
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.security import decode_token

router = APIRouter()
security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = decode_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=403, detail="Invalid token")
    return payload

@router.get("/{reg_no}")
def get_student(reg_no: str, user=Depends(get_current_user), db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.reg_no == reg_no).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return {
        "reg_no": student.reg_no,
        "name": student.name,
        "class": student.student_class,
        "blood_group": student.blood_group,
        "mobile_number": student.mobile_number,
        "parent_name": student.parent_name,
        "parent_number": student.parent_number,
        "cgpa": student.cgpa,
        "current_arrear": student.current_arrear
    }
