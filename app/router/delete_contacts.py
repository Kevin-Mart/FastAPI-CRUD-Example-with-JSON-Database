from fastapi import HTTPException
from app.lib.managedb import ManageDB

def delete_contacts(contact_id:str):
    md = ManageDB()
    contacts = md.read_contacts()
    for index, contact in enumerate(contacts):
        if contact["id"] == contact_id:
            contacts.pop(index)
            md.write_contacts(contacts)
            return {
                "success": True,
                "message": "Contact deleted successfully"
            }
    raise HTTPException(status_code=404, detail="Contact not found")