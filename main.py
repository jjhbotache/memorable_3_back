from fastapi import FastAPI,responses
from db_managment import db_managment as db
from classes.user import User
from fastapi.middleware.cors import CORSMiddleware
import os

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
    user_found = db.get_user_by_google_sub(user.google_sub)
    # if the user exists, return the user, else create a new user
    if user_found:
        return responses.JSONResponse(content={"status":"ok"})
    else:
        db.set_new_user(user)
        return responses.JSONResponse(content={"status":"ok"})
    
@app.get("/image/{name}")
def serve_image(name:str):
    path_to_img = os.path.join("designs","designs_imgs",name)
    return responses.FileResponse(path=path_to_img,media_type="image/png")

# get imgs urls
@app.get("/imgs")
def get_imgs():
    imgs = db.get_img_urls()
    print(imgs)
    return responses.JSONResponse(content=imgs)