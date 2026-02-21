#models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True, index=True)
    unique_id = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(String, default="staff")

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    reg_no = Column(String, unique=True, index=True)
    name = Column(String)
    student_class = Column(String)
    blood_group = Column(String)
    mobile_number = Column(String)
    parent_name = Column(String)
    parent_number = Column(String)
    cgpa = Column(String)
    current_arrear = Column(String)
   

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    location = Column(String)
    hod = Column(String)
    contact = Column(String)
    website = Column(String)

class Academic(Base):
    __tablename__ = "academic"
    id = Column(Integer, primary_key=True, index=True)
    syllabus_link = Column(String)
    hall_ticket_link = Column(String)
    result_link = Column(String)
    admission_pdf_link = Column(String)
    bonafide_link = Column(String)
