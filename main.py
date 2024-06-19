from fastapi import FastAPI, File, Form,responses,Request,UploadFile
from classes.design import Design
from classes.favorite_and_cart_classes_request import CrudFavoriteAndCartDesignRequest
from classes.tag import Tag
from classes.user import User
from classes.SendEmailClass import SendEmailClass
from classes.databaseConnection import DatabaseConnection 
from db_managment import db_managment as db
from fastapi.middleware.cors import CORSMiddleware
import os
from helpers.send_mail import send_email as send_mail_function
from helpers.security import decrypt_message
from helpers.compressor import *
from constants import list_of_google_sub_admins
from functools import wraps
from cloudinary_manager.cloudinary_manager import delete_file_on_cloudinary, upload_ai,upload_desing 
from fastapi.responses import FileResponse

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
    
# 
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

@app.get("/designs/public")
def get_designs_public():
    designs = db.get_designs()
    # for each design, remove the ai_url
    for design in designs:
        design["ai_url"] = ""
        
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
    db.delete_design(id_design)
    return responses.JSONResponse(content={"status":"ok"})
    
    
@app.put("/design/update")
@admin_only
def update_design(
    request:Request,
    id_design:int = Form(...),
    name:str = Form(None),
    img:UploadFile = File(None),
    ai:UploadFile = File(None),
    tags_in_string:str = Form(None), # "2,4,6,2,1,3"
    ):
    
    print("update design")
    # just print the data
    print("id_design: ",id_design)
    print("name: ",name)
    print("img: ",img)
    print("ai: ",ai)
    print("tags_in_string: ",tags_in_string)
    
    # return responses.JSONResponse(content={"status":"ok"})
    # first, parse data from the form
    # if there is a new img, upload it to cloudinary and delete the old one
    # if there is a new ai, upload it to cloudinary and delete the old one
    old_design = db.get_design_by_id(id_design)
    
    if img or ai:
        if img:
            img_url = upload_desing(img.file)
            delete_file_on_cloudinary(old_design["img_url"])
        if ai:
            ai_url = upload_ai(ai.file)
            delete_file_on_cloudinary(old_design["ai_url"])
    
    
    id_list_of_tags = [int(tag_id) for tag_id in tags_in_string.split(",")] if tags_in_string else []
    print("old_design: ",old_design)
    print("id_list_of_tags: ",id_list_of_tags)
    updatedTags = id_list_of_tags if (id_list_of_tags != None) else old_design["tags"]
    print("updatedTags: ",updatedTags)
    
    db.update_design(
        design=Design(
            id_design=id_design,
            name=name if name else old_design["name"],
            img_url=img_url if img else old_design["img_url"],
            ai_url=ai_url if ai else old_design["ai_url"]
        ),
        list_of_tags_ids=updatedTags
    )
    pass


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


@app.get("/db/export")
@admin_only
def export_db(request: Request):
    # Export the database and save it to a file
    db.export_db(
        source_path=DatabaseConnection.database_name,
        destination_path= (path_to_exported_db_file:=os.path.join(os.getcwd(),"temp", "exported_db.db"))
    )
    
    
    # Return the exported database file as a response
    return FileResponse(path_to_exported_db_file, filename="database.db")

@app.post("/db/import")
@admin_only
def import_db(request: Request, db_file: UploadFile = File(...)):
    # overwrite the current database with the uploaded file
    with open(DatabaseConnection.database_name, "wb") as f:
        f.write(db_file.file.read())    
    
    return responses.JSONResponse(content={"status":"ok"})
    
# favorite designs crud
# Add a design to the favorite list
@app.post("/favorite/add")
def add_favorite_design(request: Request, requestClass:CrudFavoriteAndCartDesignRequest):
    db.add_design_to_favorite(requestClass.user_sub, requestClass.design_id)
    return responses.JSONResponse(content={"status": "Design added to favorites"})

# Get favorite designs for a user
@app.get("/favorite/{user_sub}")
def get_favorite_design(request: Request, user_sub: str):
    designs = db.get_favorite_designs(user_sub)
    return responses.JSONResponse(content=designs)

# Remove a design from the favorite list
@app.delete("/favorite/remove")
def remove_favorite_design(request: Request, requestClass:CrudFavoriteAndCartDesignRequest):
    db.remove_design_from_favorite(requestClass.user_sub, requestClass.design_id)
    return responses.JSONResponse(content={"status": "Design removed from favorites"})


# cart designs crud
# Add a design to the cart list
@app.post("/cart/add")
def add_cart_design(request: Request, requestClass: CrudFavoriteAndCartDesignRequest):
    db.add_design_to_cart(requestClass.user_sub, requestClass.design_id)
    return responses.JSONResponse(content={"status": "Design added to cart"})

@app.get("/cart/{user_sub}")
def get_cart_design(request: Request, user_sub: str):
    designs = db.get_cart_designs(user_sub)
    return responses.JSONResponse(content=designs)

@app.delete("/cart/remove")
def remove_cart_design(request: Request, requestClass: CrudFavoriteAndCartDesignRequest):
    db.remove_design_from_cart(requestClass.user_sub, requestClass.design_id)
    return responses.JSONResponse(content={"status": "Design removed from cart"})