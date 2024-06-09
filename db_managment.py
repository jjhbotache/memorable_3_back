from classes.user import User
from classes.databaseConnection import DatabaseConnection

def get_user_by_google_sub(google_sub:str):
    connection = DatabaseConnection()
    cursor = connection.cursor
    cursor.execute(
        "SELECT * FROM users WHERE google_sub = ?",
        (google_sub,)
    )
    user = cursor.fetchone()
    connection.connection.close()
    return user

def set_new_user(user:User):
    connection = DatabaseConnection()
    connection.cursor.execute(
        "INSERT INTO users (google_sub, name, email, phone, image_url) VALUES (?, ?, ?, ?, ?)",
        (user.google_sub, user.name, user.email, user.phone, user.image_url)
    )
    connection.connection.commit()
    connection.connection.close()