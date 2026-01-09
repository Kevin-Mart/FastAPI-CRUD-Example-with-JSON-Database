# FastAPI CRUD Examples

This repository contains **multiple FastAPI CRUD example projects**, created for learning and practice purposes.  
Each project demonstrates how to build a RESTful API using FastAPI with different data persistence approaches.

---

## 🚀 Projects Included

### 📁 1. FastAPI CRUD with JSON Database

A simple CRUD API that uses a **JSON file as a mock database**, ideal for beginners and quick prototyping.

**Highlights:**

- No external database required
- Easy to understand and lightweight
- Focused on FastAPI fundamentals

---

### 📁 2. FastAPI CRUD with PostgreSQL

A more advanced CRUD API that uses **PostgreSQL as a relational database**, suitable for real-world backend development practices.

**Highlights:**

- PostgreSQL integration
- Database-driven CRUD operations
- Scalable and closer to production-ready architecture

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- JSON (mock database)
- PostgreSQL
- psycopg / SQL tools (depending on implementation)

---

## 📂 Repository Structure

```text
backend/
├── fastapi-json/                              # FastAPI CRUD using JSON as database
│   ├── main.py                       # Application entry point
│   │
│   ├── lib/
│   │   └── managedb.py               # JSON database management logic
│   │
│   ├── db/
│   │   └── dbContacts.json           # Mock database (JSON file)
│   │
│   └── router/                       # API route handlers
│       ├── get_contacts.py           # Get all contacts
│       ├── get_contact.py            # Get a single contact
│       ├── post_contacts.py          # Create a new contact
│       ├── put_contacts.py           # Update an existing contact
│       └── delete_contacts.py        # Delete a contact
│
├── FASTAPI-POSTGRES/                 # FastAPI CRUD using PostgreSQL
│   ├── config/
│   │   └── __init__.py               # Application configuration and settings
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   └── user_connection.py        # PostgreSQL connection and database logic
│   │
│   ├── schema/
│   │   ├── __init__.py
│   │   └── user_schema.py            # Pydantic schemas for data validation
│   │
│   ├── main.py                       # FastAPI application entry point (PostgreSQL)
│   └── fastapi-postgres.sql          # SQL script to create database tables
│
├── .gitignore
├── README.md

```

## ▶️ How to Run the Project

#### 1. Clone the repository:

```
git clone https://github.com/Kevin-Mart/FastAPI-CRUD-Example-with-JSON-Database.git
```

#### 2. Move into the backend directory:

```
cd backend
```

#### 3. Create and activate a virtual environment (optional but recommended)

#### 4. Install dependencies:

```
pip install fastapi uvicorn
```

#### 5. Run the application:

```
uvicorn app.main:app --reload
```

#### 6. Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

### ⚠️ Disclaimer

This project is not intended for production use.
Using a JSON file as a database is only suitable for testing and learning scenarios.
