from fastapi import FastAPI, File, Form,responses,Request,UploadFile
from classes.design import Design
from classes.tag import Tag
from db_managment import db_managment as db
from classes.user import User
from classes.SendEmailClass import SendEmailClass
from fastapi.middleware.cors import CORSMiddleware
import os
from helpers.send_mail import send_email as send_mail_function
from helpers.security import decrypt_message
from helpers.compressor import *
from constants import list_of_google_sub_admins
from functools import wraps
from cloudinary_manager.cloudinary_manager import delete_file_on_cloudinary, upload_ai,upload_desing 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def admin_only(func):
    @wraps(func) # this is to keep the original function name and info
    def new_func(*args,**kwargs):
        real_list_of_google_sub_admins = [ decrypt_message(admin) for admin in list_of_google_sub_admins]
        request:Request = kwargs["request"]
        google_sub = request.headers["google_sub"]
        # print("real_list_of_google_sub_admins: ",real_list_of_google_sub_admins)
        # print("headers: ",request.headers)
        # print("google_sub: ",google_sub)
        print(request.headers["google_sub"] in real_list_of_google_sub_admins)
        if request.headers["google_sub"] in real_list_of_google_sub_admins:
            return func(*args,**kwargs)
        else:
            return responses.JSONResponse(content={"status":"not allowed, only for admin"},status_code=401)
        
    return new_func

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

@app.get("/imgs")
def get_imgs():
    # get all the imgs from the designs
    get_imgs = db.get_img_urls()
    return responses.JSONResponse(content=get_imgs)


@app.post("/contact-us")
def send_email(data:SendEmailClass):
    data.recipent = "memorableibaguecolombia@gmail.com"
    send_mail_function(
        recipent=data.recipent,
        subject=data.subject,
        message=data.message
    )
    return responses.JSONResponse(content={"status":"ok"})


# tags
@app.get("/tags")
def get_tags():
    print("get tags")
    tags = db.get_tags_from_db()
    return responses.JSONResponse(content=tags)

@app.post("/tag/create")
@admin_only
def create_tag(tag:Tag,request:Request):
    
    db.set_tag(tag)
    return responses.JSONResponse(content={"status":"ok"})

@app.put("/tag/update")
@admin_only
def update_tag(tag:Tag,request:Request):
    db.update_tag_in_db(tag)
    return responses.JSONResponse(content={"status":"ok"})

@app.delete("/tag/delete")
@admin_only
def delete_tag(tag:Tag,request:Request):
    db.delete_tag(tag)
    return responses.JSONResponse(content={"status":"ok"})  

# designs
@app.get("/designs")
@admin_only
def get_designs(request:Request):
    designs = db.get_designs()
    return responses.JSONResponse(content=designs)

@app.post("/design/create")
@admin_only
def create_design(
    request:Request,
    name:str = Form(...),
    img:UploadFile = File(...),
    ai:UploadFile = File(...),
    tags_in_string:str = Form(None), # 2,4,6,2,1,3
    ):
    print("create design")
    
    current_dir = os.getcwd()
    
    # create a list of id tags
    tags_id = [ int(tag_id.strip()) for tag_id in tags_in_string.split(",")] if tags_in_string else []
    
    # create a compressed version of the ai file
    # send the compressed version of the AI and the img to the cloudinary
    # delete the compressed version of the AI
    # create the design in the db with the cloudinary urls and the name
    # create the tags related to the design

    # temporary save the files
    ai_path = "./temp/"+name+".ai"
    img_path = "./temp/"+name+".png"
    with open(ai_path,"wb") as f: f.write(ai.file.read())
    with open(img_path,"wb") as f: f.write(img.file.read())
    # compress the AI file
    
    # await compress_to_gzip(ai_path, "./temp/")
    # os.remove(ai_path)
    
    
    # send the files to cloudinary
    ai_url = upload_ai(os.path.join(current_dir,"temp",name+".ai"))
    img_url = upload_desing(os.path.join(current_dir,"temp",name+".png"))
    
    # delete the compressed version of the AI
    os.remove(ai_path)
    os.remove(img_path)
    
    
    # create the design in the db
    db.set_design(
        design=Design(
            id_design=0,
            name=name,
            img_url= img_url,
            ai_url=ai_url
        ),
        list_of_tags_ids=tags_id
    )
    
    return responses.JSONResponse(content={"status":"ok"})

@app.delete("/design/delete/{id_design}")
@admin_only
def delete_design(id_design:int,request:Request):
    # delete each file on cloudinary
    design = db.get_design_by_id(id_design)
    print("design: ",design)
    delete_file_on_cloudinary(design["img_url"])
    delete_file_on_cloudinary(design["ai_url"])  
    
    db.delete_design(id_design)
    return responses.JSONResponse(content={"status":"ok"})


# users crud
@app.get("/users")
@admin_only
def get_users(request:Request):
    users = db.get_users()
    return responses.JSONResponse(content=users)

@app.delete("/user/delete/{google_sub}")
@admin_only
def delete_user(google_sub:str,request:Request):
    db.delete_user(google_sub)
    return responses.JSONResponse(content={"status":"ok"})

@app.put("/user/update")
@admin_only
def update_user(user:User,request:Request):
    db.update_user(user)
    return responses.JSONResponse(content={"status":"ok"})

# route to verify the user is an admin or not
@app.get("/verify-admin")
@admin_only
def verify_admin(request:Request):
    return responses.JSONResponse(content={"status":"ok"})