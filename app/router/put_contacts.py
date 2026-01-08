from app.lib.managedb import ManageDB
from fastapi import HTTPException

def put_contacts(id_contact, updated_contact):
    md = ManageDB()
    contacts = md.read_contacts()
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = updated_contact.dict()

            if updated_contact.name == "":
                contacts[index]["name"] = contact["name"]   
            if updated_contact.email == "":
                contacts[index]["email"] = contact["email"] 
            if updated_contact.phone == "":
                contacts[index]["phone"] = contact["phone"]

            md.write_contacts(contacts)
            return {
                "success": True,
                "message": "Contact updated successfully"
            }
        
    raise HTTPException(status_code=404, detail="Contact not found")