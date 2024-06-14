import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url
import os
import dotenv
dotenv.load_dotenv()
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
# Configuration       
cloudinary.config( 
    cloud_name = "dgm8uzbpd", 
    api_key = "189257474116189", 
    api_secret = CLOUDINARY_API_SECRET,
    secure=True
)

def upload_desing(file_path:str):
    response = cloudinary.uploader.upload(file_path, folder="designs")
    return response["url"]
  
def upload_ai(file_path:str):
    response = cloudinary.uploader.upload(file_path, folder="ais")
    return response["url"]

def delete_file_on_cloudinary(public_url):
    # "http://res.cloudinary.com/dgm8uzbpd/image/upload/v1718382248/designs/xugpez0dz1sxksdh30ha.png"
    public_id = "/".join(public_url.split('/')[-2:]).split('.')[0]
    result = cloudinary.api.delete_resources([public_id])
    return result
    

    