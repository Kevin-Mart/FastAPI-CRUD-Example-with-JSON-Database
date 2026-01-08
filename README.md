# FastAPI CRUD Example with JSON Database

This project is a simple **CRUD (Create, Read, Update, Delete) API built with FastAPI in Python**.  
It is designed as a learning and practice example, using a **JSON file as a mock database** instead of a traditional DBMS.

---

## 🚀 Features

- CRUD operations (Create, Read, Update, Delete)
- RESTful API architecture
- FastAPI framework
- JSON file used as a lightweight data store
- Modular and easy-to-understand project structure

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- JSON (mock database)

---

## 📂 Project Structure

```text
backend/
├── app/
│   ├── main.py              # Application entry point
│   │
│   ├── lib/
│   │   └── managedb.py      # JSON database management logic
│   │
│   ├── db/
│   │   └── dbContacts.json  # Mock database (JSON file)
│   │
│   └── router/
│       ├── get_contacts.py      # Get all contacts
│       ├── get_contact.py       # Get a single contact
│       ├── post_contacts.py     # Create a new contact
│       ├── put_contacts.py      # Update an existing contact
│       └── delete_contacts.py   # Delete a contact
│
└── README.md
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

### 📌 Purpose

This project is intended for educational purposes only, to demonstrate how FastAPI works and how CRUD operations can be implemented without the complexity of a real database.

### ⚠️ Disclaimer

This project is not intended for production use.
Using a JSON file as a database is only suitable for testing and learning scenarios.
