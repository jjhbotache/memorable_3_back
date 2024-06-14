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
    # Extraer el ID público del archivo de la URL
    # Asumiendo que la URL sigue el formato estándar de Cloudinary
    partes_url = public_url.split('/')
    public_id = partes_url[-1].split('.')[0]  # Elimina la extensión del archivo

    # Eliminar el archivo usando Cloudinary
    result = cloudinary.uploader.destroy(public_id) 
    return result
    

    