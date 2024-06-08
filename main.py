from fastapi import FastAPI,responses
import back.db_managment as db # type: ignore
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
 
@app.post("/user-login-signup")
def get_set_user(user:User):
    print(user)
    user_found = db.get_user_by_google_sub(user.google_sub)
    # if the user exists, return the user, else create a new user
    if user_found:
        return responses.JSONResponse(content={"status":"ok"})
    else:
        db.set_new_user(user)
        return responses.JSONResponse(content={"status":"ok"})