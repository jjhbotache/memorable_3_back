import requests
import base64
import requests
import base64

def image_to_base64(image_path):
  with open(image_path, "rb") as image:
    base64_image = base64.b64encode(image.read()).decode('utf-8')
  return base64_image


def url_to_base64(image_url):
  response = requests.get(image_url)
  base64_image = base64.b64encode(response.content).decode('utf-8')
  return str(base64_image)