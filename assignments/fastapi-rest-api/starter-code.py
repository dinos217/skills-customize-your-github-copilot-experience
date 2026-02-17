from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

# Initialize FastAPI application
app = FastAPI(title="Student Management API")

# Define data models using Pydantic
class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    enrollment_date: date

class Student(StudentCreate):
    id: int

# In-memory database (list to store students)
students_db: List[dict] = []
student_id_counter = 1

# Task 1: Basic Endpoints
@app.get("/")
def welcome():
    """Welcome endpoint - returns a greeting message"""
    return {"message": "Welcome to Student Management API", "course": "Computer Science"}

@app.post("/greet")
def greet_student(name: str):
    """Simple POST endpoint that accepts a student name"""
    return {"message": f"Hello, {name}! Welcome to the course."}

# Task 2: CRUD Operations (TODO: Implement these endpoints)
# @app.post("/students", status_code=status.HTTP_201_CREATED)
# def create_student(student: StudentCreate):
#     # Add implementation here
#     pass

# @app.get("/students")
# def get_all_students():
#     # Add implementation here
#     pass

# @app.get("/students/{student_id}")
# def get_student(student_id: int):
#     # Add implementation here
#     pass

# @app.put("/students/{student_id}")
# def update_student(student_id: int, student: StudentCreate):
#     # Add implementation here
#     pass

# @app.delete("/students/{student_id}")
# def delete_student(student_id: int):
#     # Add implementation here
#     pass

# Run the application with: uvicorn starter-code:app --reload
