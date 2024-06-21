import google.generativeai as genai
import os
import dotenv
import pprint

from db_managment.db_managment import get_designs
# from db_managment import get_designs


dotenv.load_dotenv()
PALM_API_KEY = os.getenv('PALM_API_KEY')
genai.configure(api_key=PALM_API_KEY)


# make code to choose the model
model = genai.GenerativeModel('gemini-1.5-flash')




def tags_to_str(tags):
    return ", ".join([tag["name"] for tag in tags])



# # Create a new conversation


def search_designs_with_ai(searched_text:str):
  # print usefull models
  # models = genai.list_models()
  # for model in [m for m in models if "generateContent" in m.supported_generation_methods or "generateText" in m.supported_generation_methods]:
  #   print(model)
  
  
    
  designs = get_designs(None)
  desings_str = "\n".join([f"-{design['id']}){design['name']} - ({ tags_to_str(design['tags']) })" for design in designs])
  response = model.generate_content(f"""
Hay una persona que esta buscando un diseño: "{searched_text}".
Existen estos diseños con estas tags:
{desings_str}
no respondas nada mas que una lista en este formato con los numeros de diseño que le sevirian a la persona:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]""".strip())
  try:
    raw_response = response.text
    only_list_response = raw_response.split("]")[0].split("[")[1]
    list_response = only_list_response.split(",")
    list_response = [int(i) for i in list_response]
    
    filtered_designs = [design for design in designs if design['id'] in list_response]
  except Exception as e:
    print("Error")
    print(e)
    filtered_designs = []
  return filtered_designs