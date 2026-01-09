from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_204_NO_CONTENT
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection()

@app.get("/",status_code=HTTP_200_OK)
def read_root():
    conn
    return {"message": "Hello World"}

@app.post("/api/insert_user",status_code=HTTP_201_CREATED)
def insert_user(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id", None)  # Remove 'id' if present
    conn.wrtite_db(data)
    return Response(status_code=HTTP_201_CREATED)

@app.get("/api/get_users", status_code=HTTP_200_OK)
def get_users():
    records = conn.read_db()
    return {"users": records}

@app.get("/api/get_user/{user_id}",status_code=HTTP_200_OK)
def get_user(user_id):
    records =conn.read_byid_db(user_id)
    return records

@app.delete("/api/delete_user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id):
    conn.delete_bd(user_id)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.put("/api/update_user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def updateUser(user_id, user_data: UserSchema):
    data = user_data.dict()
    data["id"] = user_id
    conn.update_bd(data)
    return Response(status_code=HTTP_204_NO_CONTENT)