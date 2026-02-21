# chatbot_service.py (Hybrid Version)
from models import Department, Academic, Student
from database import SessionLocal
from sqlalchemy.orm import Session
import difflib

# ---------------- INTENTS ----------------
INTENTS = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "total_department": ["total department", "how many department", "number of department", "departments count"],
    "total_student": ["total student", "how many student", "student count", "students total"],
    "hod": ["hod", "head", "head of department", "hod no", "hod contact", "head contact"],
    "contact": ["contact", "phone", "mobile", "number", "cell"],
    "location": ["where", "location", "situated", "address"],
    "website": ["website", "site", "link", "url"],
    "details": ["about", "details", "tell me about", "info", "information"],
    "syllabus": ["syllabus", "curriculum"],
    "result": ["result", "exam result", "grades", "marks"],
    "hall_ticket": ["hall ticket", "admit card", "exam card"],
    "admission": ["admission", "apply", "registration", "form"],
    "bonafide": ["bonafide", "certificate"]
}

# ---------------- DEPARTMENT ALIASES ----------------
DEPT_ALIASES = {
    "computer science": ["cse", "cs", "comp sci", "computer", "cs dept", "computer science department"],
    "mechanical": ["mech", "mechanical eng", "mechanical dept"],
    "electronics": ["ece", "electronics and communication", "electronics dept"],
    "civil": ["civil eng", "civil dept"],
    "information technology": ["it", "it dept", "information tech", "information technology dept"]
}

# ---------------- NORMALIZATION ----------------
def normalize(text: str):
    return text.lower().strip()

def match_intent(query, intent_name):
    return any(keyword in query for keyword in INTENTS[intent_name])

# ---------------- FIND DEPARTMENT ----------------
def find_department_from_query(query, departments):
    # 1️⃣ Direct match
    for dept in departments:
        if dept.name.lower() in query:
            return dept

    # 2️⃣ Alias match
    for dept in departments:
        dept_name = dept.name.lower()
        if dept_name in DEPT_ALIASES:
            for alias in DEPT_ALIASES[dept_name]:
                if alias in query:
                    return dept

    # 3️⃣ Fuzzy match (typo handling)
    dept_names = [dept.name.lower() for dept in departments]
    words = query.split()
    for word in words:
        close_match = difflib.get_close_matches(word, dept_names, n=1, cutoff=0.7)
        if close_match:
            for dept in departments:
                if dept.name.lower() == close_match[0]:
                    return dept

    return None

# ---------------- HANDLE QUERY ----------------
def handle_query(query: str):
    db: Session = SessionLocal()
    query = normalize(query)

    departments = db.query(Department).all()
    academics = db.query(Academic).first()
    students = db.query(Student).all()

    # ---------------- GREETING ----------------
    if match_intent(query, "greeting"):
        db.close()
        return "Hello! Welcome to CampusConnect. How can I assist you?"

    # ---------------- TOTAL DEPARTMENTS ----------------
    if match_intent(query, "total_department"):
        db.close()
        return f"Total number of departments: {len(departments)}"

    # ---------------- TOTAL STUDENTS ----------------
    if match_intent(query, "total_student"):
        db.close()
        return f"Total number of students: {len(students)}"

    # ---------------- DEPARTMENT SPECIFIC ----------------
    dept = find_department_from_query(query, departments)

    if dept:
        # Map intent to department attribute
        if match_intent(query, "hod"):
            db.close()
            return f"HOD of {dept.name}: {dept.hod}"

        if match_intent(query, "contact"):
            db.close()
            return f"Contact number of {dept.name}: {dept.contact}"

        if match_intent(query, "location"):
            db.close()
            return f"{dept.name} is located at: {dept.location}"

        if match_intent(query, "website"):
            db.close()
            return f"Website of {dept.name}: {dept.website}"

        if match_intent(query, "details"):
            db.close()
            return (
                f"{dept.name} Department:\n"
                f"HOD: {dept.hod}\n"
                f"Location: {dept.location}\n"
                f"Contact: {dept.contact}\n"
                f"Website: {dept.website}"
            )

        # Default response if user just mentions department
        db.close()
        return f"{dept.name} department is available. You can ask about HOD, contact, location, website, or details."

    # ---------------- LIST ALL DEPARTMENTS ----------------
    if "department" in query or "departments" in query:
        names = [dept.name for dept in departments]
        db.close()
        return f"Departments available: {', '.join(names)}"

    # ---------------- ACADEMIC INFORMATION ----------------
    if academics:
        if match_intent(query, "syllabus"):
            db.close()
            return f"Syllabus link: {academics.syllabus_link}"

        if match_intent(query, "result"):
            db.close()
            return f"Result link: {academics.result_link}"

        if match_intent(query, "hall_ticket"):
            db.close()
            return f"Hall Ticket link: {academics.hall_ticket_link}"

        if match_intent(query, "admission"):
            db.close()
            return f"Admission form link: {academics.admission_pdf_link}"

        if match_intent(query, "bonafide"):
            db.close()
            return f"Bonafide form link: {academics.bonafide_link}"

    db.close()
    return "Sorry, I could not understand your query. Please try asking in a different way."
