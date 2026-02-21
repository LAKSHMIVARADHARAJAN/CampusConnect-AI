from database import Base, engine
from models import Staff, Student, Department, Academic  # import all models

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")
