import requests
import dotenv
import os

dotenv.load_dotenv()



api_url = "https://script.google.com/macros/s/AKfycbyoBhxuklU5D3LTguTcYAS85klwFINHxxd-FroauC4CmFVvS0ua/exec"
WHATS_TOKEN = os.getenv("WHATS_TOKEN")

def send_whats_msg(phone, msg:str):
  payload = {
    "op": "registermessage",
    "token_qr": WHATS_TOKEN, "mensajes": 
      [
        {"numero": f"57{phone}","mensaje": msg},
        # {"numero": "51986321853","url": "https://as01.epimg.net/meristation/imagenes/2021/06/04/noticias/1622794682_038694_1622794767_noticia_normal.jpg"},
        # {"numero": "51986321853","imagenbase64": "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"}
      ]
    }
  response = requests.post(api_url, json=payload)
  return response.json()

def send_whats_img(phone, imgBase64:str):
  payload = {
    "op": "registermessage",
    "token_qr": WHATS_TOKEN, "mensajes": 
      [
        {"numero": f"57{phone}","imagenbase64": imgBase64},
        # {"numero": "51986321853","url": "https://as01.epimg.net/meristation/imagenes/2021/06/04/noticias/1622794682_038694_1622794767_noticia_normal.jpg"},
        # {"numero": "51986321853","imagenbase64": "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"}
      ]
    }
  response = requests.post(api_url, json=payload)
  return response.json()


def confirm_buyment(
  phone,
  img_base_64:str,
  design_id:int,
  quantity:int,
  wine:str,
  buy:bool,
  name:str=None
  ):
  
  if buy:
    main_msg = f"Hemos recibido tu solicitud de compra del diseño #{design_id} de {quantity} botellas de {wine}. En breve nos pondremos en contacto contigo para coordinar la entrega!."
  else:
    main_msg = f"Hemos recibido tu solicitud para modificar este diseño({design_id}). En breve nos pondremos en contacto contigo para coordinar los detalles!."
  
  # capitalize first letters of name
  name = name.title() if name else None
  
  payload = {
    "op": "registermessage",
    "token_qr": WHATS_TOKEN, "mensajes": 
      [
        {"numero": f"57{phone}","imagenbase64": img_base_64},
        {"numero": f"57{phone}","mensaje": f"""
         🍷🌟¡Hola {name+"!" if name else '!'}\n{main_msg}         
         """.strip()},        
      ]
    }
  print(payload)
  response = requests.post(api_url, json=payload)
  print(response.__dict__)
  return response.json()