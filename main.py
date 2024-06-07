from fastapi import FastAPI,responses
import back.db_managment as db
from .classes.user import User
from .classes.data import Data
from .classes.create_data import CreateData
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
 
# crud for users
@app.post("/users/create")
def create_user(user: User):
    try:
        db.create_user(user.username, user.password)
    except ValueError as e:
        return {"error": str(e)}
    
    return {"message": "User created"}

@app.post("/users/read")
def read_user(user: User):
    result = db.read_user(user.username, user.password)
    if not result:
        # return an error code
        return responses.JSONResponse(status_code=404, content={"error": "User not found"})
    else:
        # get the user data
        user_data = db.read_data(result["id"], user.password)
        return {
            "message": "User found",
            "user": result,
            "data": user_data
            }

@app.put("/users/update")
def update_user(user: User, new_user: User):
    db.update_user(user.username, user.password, new_user.username, new_user.password)
    return {"message": "User updated"}

@app.delete("/users/delete")
def delete_user(user: User):
    db.delete_user(user.username, user.password)
    return {"message": "User deleted"}
    
# crud for data
@app.post("/data/create")
def create_data(create_data: CreateData):
    try:
        db.create_data(create_data.user_id, create_data.password, create_data.email, create_data.address, create_data.phone)
    except ValueError as e:
        return {"error": str(e)}
    
    return {"message": "Data created"}

@app.post("/data/read")
def read_data(data: Data):
    result = db.read_data(data.username)
    if not result:
        return {"error": "Data not found"}
    else:
        return {"message": "Data found", "data": result}

@app.put("/data/update")
def update_data(data: Data, new_data: Data):
    db.update_data(data.username, data.data, new_data.data)
    return {"message": "Data updated"}

@app.delete("/data/delete")
def delete_data(data: Data):
    db.delete_data(data.username, data.data)
    return {"message": "Data deleted"}