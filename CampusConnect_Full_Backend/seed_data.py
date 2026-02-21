from database import SessionLocal
from models import Staff, Student, Department, Academic
from utils.security import hash_password

db = SessionLocal()

# ---------------- STAFF ----------------
staff1 = Staff(
    unique_id="staff01",
    password=hash_password("1234"),
    role="staff"
)

# ---------------- DEPARTMENT ----------------
dept1 = Department(
    name="Computer Science Engineering",
    location="Block A",
    hod="Dr. Kumar",
    contact="9876543210",
    website="www.csecollege.com"
)

dept2 = Department(
    name="Mechanical Engineering",
    location="Block B",
    hod="Dr. Ravi",
    contact="9876500000",
    website="www.mechcollege.com"
)

# ---------------- ACADEMIC ----------------
academic = Academic(
    syllabus_link="www.college.com/syllabus",
    hall_ticket_link="www.college.com/hallticket",
    result_link="www.college.com/results",
    admission_pdf_link="www.college.com/admission",
    bonafide_link="www.college.com/bonafide"
)

# ---------------- STUDENTS ----------------
student1 = Student(
    reg_no="22CS101",
    name="Arun Kumar",
    student_class="III CSE",
    blood_group="O+",
    mobile_number="9876543210",
    parent_name="Ramesh",
    parent_number="9876500000",
    cgpa="8.4",
    current_arrear="0"
)

student2 = Student(
    reg_no="22CS102",
    name="Priya Sharma",
    student_class="III CSE",
    blood_group="A+",
    mobile_number="9876511111",
    parent_name="Suresh",
    parent_number="9876522222",
    cgpa="8.9",
    current_arrear="1"
)

student3 = Student(
    reg_no="22ME201",
    name="Karthik Raj",
    student_class="III MECH",
    blood_group="B+",
    mobile_number="9876533333",
    parent_name="Manoj",
    parent_number="9876544444",
    cgpa="7.8",
    current_arrear="2"
)

# ---------------- ADD TO DATABASE ----------------
db.add_all([
    staff1,
    dept1, dept2,
    academic,
    student1, student2, student3
])

db.commit()
db.close()

print("✅ All data inserted successfully!")
