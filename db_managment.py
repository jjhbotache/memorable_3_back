import sqlite3

class DatabaseConnection:
    _instance = None
    
    def __new__(cls): # this method is called before __init__
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = sqlite3.connect('data.db')
        return cls._instance
    
    def __init__(self):
        self.cursor = self.connection.cursor()


def authenticate_user(func):
    def wrapper(user_id, password,*args, **kwargs):
        # get the user from the id and password
        db = DatabaseConnection()
        user = db.cursor.execute(" SELECT * FROM users WHERE id = ? AND password = ? ", (user_id, password)).fetchone()
        if user is not None:
            return func(user_id, password,*args)
        else:
            raise ValueError(f"Invalid credentials while authenticating user in {func.__name__}")
    
    return wrapper

# create CRUD functions for data
def fetch_data_as_dict(cursor, query, params=None):
    cursor.execute(query, params if params else [])
    columns = [column[0] for column in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    print(result)
    return result

@authenticate_user
def create_data(user_id,password, email, address, phone):
    db = DatabaseConnection()
    db.cursor.execute("""
                   INSERT INTO data (user_id, email, address, phone)
                   VALUES (?, ?, ?, ?)
                   """, (user_id, email, address, phone))
    db.connection.commit()

@authenticate_user
def read_data(user_id,password):
    db = DatabaseConnection()
    return fetch_data_as_dict(db.cursor, """
                   SELECT * FROM data
                   WHERE user_id = ?
                   """, (user_id,))[0]

def update_data(data_id, email, address, phone):
    db = DatabaseConnection()
    db.cursor.execute("""
                   UPDATE data
                   SET email = ?, address = ?, phone = ?
                   WHERE data_id = ?
                   """, (email, address, phone, data_id))
    db.connection.commit()

def delete_data(data_id):
    db = DatabaseConnection()
    db.cursor.execute("""
                   DELETE FROM data
                   WHERE data_id = ?
                   """, (data_id,))
    db.connection.commit()

def create_user(username:str, password:str):
    db = DatabaseConnection()
    existing_user = db.cursor.execute(" SELECT * FROM users WHERE username = ? ", (username,)).fetchone()
    if existing_user: raise ValueError("User already exists")

    db.cursor.execute("""
                   INSERT INTO users (username, password)
                   VALUES (?, ?)
                   """, (username, password))
    db.connection.commit()

def read_user(username, password):
    db = DatabaseConnection()
    try:
        return fetch_data_as_dict(db.cursor, f"""
                        SELECT * FROM users
                        WHERE username = '{username}' AND password = '{password}'
                        """)[0]
    except IndexError:
        return None
        

def update_user(username, password, new_username, new_password):
    db = DatabaseConnection()
    db.cursor.execute(f"""
                       UPDATE users
                       SET username = '{new_username}', password = '{new_password}'
                       WHERE username = '{username}' AND password = '{password}'
                       """)
    db.connection.commit()

def delete_user(username, password):
    db = DatabaseConnection()
    db.cursor.execute("""
                   DELETE FROM users
                   WHERE username = ? AND password = ?
                   """, (username, password))
    db.connection.commit()
