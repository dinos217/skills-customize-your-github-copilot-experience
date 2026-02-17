# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI to understand HTTP methods, request/response handling, and API design principles.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application and Basic Endpoints

#### Description
Create a FastAPI application with basic GET and POST endpoints to understand how to structure a simple API.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Create a GET endpoint that returns a welcome message with the course name
- Create a POST endpoint that accepts a JSON request with a student name and returns a confirmation message
- Run the application on localhost:8000 and test endpoints using a REST client or curl


### 🛠️ Implement CRUD Operations for Student Records

#### Description
Build endpoints to create, read, update, and delete student records in a simple data structure (list or dictionary).

#### Requirements
Completed program should:

- Create a POST endpoint to add a new student (with name, email, and enrollment date)
- Create a GET endpoint to retrieve all students
- Create a GET endpoint to retrieve a specific student by ID
- Create a PUT endpoint to update a student's information
- Create a DELETE endpoint to remove a student from the system
- Include appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Add Error Handling and Validation

#### Description
Implement proper error handling and input validation to make the API robust and user-friendly.

#### Requirements
Completed program should:

- Validate that required fields (name, email) are provided and properly formatted
- Return appropriate error responses with meaningful messages for invalid requests
- Handle cases where a student ID does not exist
- Use FastAPI's validation features (Pydantic models) to enforce data types and structure
- Demonstrate proper error responses with HTTP status codes (400, 404, 500)
