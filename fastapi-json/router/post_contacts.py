from app.lib.managedb import ManageDB

def post_contacts(new_contact):
    md = ManageDB()
    contacts = md.read_contacts()
    new_contact= new_contact.dict()
    contacts.append(new_contact)
    md.write_contacts(contacts)

    return{
        "success": True,
        "message": "Contact created successfully"
    }