from app.lib.managedb import ManageDB

def get_contacts():
    md = ManageDB()
    return md.read_contacts()
