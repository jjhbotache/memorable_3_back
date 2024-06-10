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
    
def get_img_urls():
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute( "SELECT * FROM designs" )
    img_urls = cursor.fetchall()
    # organize the data in dicts
    columns = [column[0] for column in cursor.description]
    img_urls = [dict(zip(columns, row)) for row in img_urls]
    db.connection.close()
    return img_urls