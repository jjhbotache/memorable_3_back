import os

FILE_NAME = "token.bin"

def create_token(token):
  if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "wb") as file:
      file.write(token.encode())
    return True
  return False

def read_token():
  if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "rb") as file:
      return file.read().decode()
  return None

def update_token(new_token):
  if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "wb") as file:
      file.write(new_token.encode())
    return True
  return False

def delete_token():
  if os.path.exists(FILE_NAME):
    os.remove(FILE_NAME)
    return True
  return False
