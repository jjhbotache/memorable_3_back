from pathlib import Path

FILE_NAME = "token.bin"

def create_token(token):
  file_path = Path(FILE_NAME)
  if not file_path.exists():
    with file_path.open("wb") as file:
      file.write(token.encode())
    return True
  return False

def read_token():
  file_path = Path(FILE_NAME)
  if file_path.exists():
    with file_path.open("rb") as file:
      return file.read().decode()
  return None

def update_token(new_token):
  file_path = Path(FILE_NAME)
  if file_path.exists():
    with file_path.open("wb") as file:
      file.write(new_token.encode())
    return True
  return False

def delete_token():
  file_path = Path(FILE_NAME)
  if file_path.exists():
    file_path.unlink()
    return True
  return False
