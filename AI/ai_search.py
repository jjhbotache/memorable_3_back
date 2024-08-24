import time
import os
import dotenv
import cohere
from db_managment.db_managment import get_designs


dotenv.load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')

co = cohere.Client(COHERE_API_KEY)


def search_designs_with_ai(searched_text:str):
  designs, desings_str = get_design_str()
  prompt = f"""
  Hay una persona que esta buscando un diseño: "{searched_text}".
  Existen estos diseños con estas tags:
  {desings_str}
  no respondas nada mas que una lista en este formato con los numeros de diseño que podria estar buscando la persona:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]""".strip()
  
  
  for _ in range(3):
    try:
      response = co.chat(message=prompt).text
      break
    except Exception as e:
      print("Error on cohere: ", e)
      time.sleep(5)
  
  try:
    only_list_response = response.split("]")[0].split("[")[1]
    list_response = only_list_response.split(",")
    list_response = [int(i) for i in list_response]
    filtered_designs = [design for design in designs if design['id'] in list_response]
  except Exception as e:
    print("Error")
    print(e)
    filtered_designs = []
  return filtered_designs



def get_design_str():
    designs = get_designs(None)
    desings_str = "\n".join([f"-{design['id']}){design['name']} - ({ tags_to_str(design['tags']) })" for design in designs])
    return designs,desings_str
  
def tags_to_str(tags):
  return ", ".join([tag["name"] for tag in tags])



if __name__ == "__main__":
  print(search_designs_with_ai("Amor"))