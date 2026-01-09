from fastapi import FastAPI, HTTPException
from app.lib.managedb import ManageDB
from pydantic import BaseModel
from uuid import uuid4  as uuid

from app.router.get_contact import get_contact
from app.router.get_contacts import get_contacts
from app.router.post_contacts import post_contacts
from app.router.put_contacts import put_contacts
from app.router.delete_contacts import delete_contacts

class ContactModel(BaseModel):
    id: str = str(uuid())
    name: str
    email: str
    phone: str

app = FastAPI()
md = ManageDB()

@app.get("/")
def read_root():
    return {"message": "HelloWorld"}

@app.get("/api/contacts")
def get_all_contacts():
     return get_contacts()

@app.get("/api/contacts/{contact_id}")
def get_single_contact(contact_id):
    return get_contact(contact_id)

@app.post("/api/contacts")
def create_contact(new_contact: ContactModel):
    post_contacts(new_contact)

@app.put("/api/contacts/{contact_id}")
def update_contact(contact_id, updated_contact: ContactModel):
   put_contacts(contact_id, updated_contact)

@app.delete("/api/contacts/{contact_id}")
def delete_contact(contact_id:str):
    return delete_contacts(contact_id)    