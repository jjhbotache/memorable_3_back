from classes.user import User
from classes.databaseConnection import DatabaseConnection
from classes.design import Design
from classes.tag import Tag


def get_user_by_google_sub(google_sub: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "SELECT * FROM users WHERE google_sub = %s",
        (google_sub,)
    )
    user = cursor.fetchone()
    
    # parse the user data to a User object
    if user is not None:
        user = dict(zip([column[0] for column in cursor.description], user))
        
    db.close_connection()
    return user


def get_img_urls():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT img_url FROM designs")
    img_urls = cursor.fetchall()
    db.close_connection()
    return img_urls


# tags
def set_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO tags (name) VALUES (%s)",
        (tag.name,)
    )
    db.get_connection().commit()
    tag.id_tag = cursor.lastrowid
    db.close_connection()
    return tag

def get_tags_from_db():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM tags")
    tags = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    tags = [dict(zip(columns, row)) for row in tags]
    db.close_connection()
    return tags

def update_tag_in_db(tag: Tag):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE tags SET name = %s WHERE id = %s",
        (tag.name, tag.id_tag)
    )
    db.get_connection().commit()
    db.close_connection()

def delete_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM tags WHERE id = %s",
        (tag.id_tag,)
    )
    db.get_connection().commit()
    db.close_connection()

def get_tags_by_design_id(id_design: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """
        SELECT tags.id, tags.name
        FROM tag_design 
        JOIN tags ON tag_design.id_tag = tags.id
        WHERE tag_design.id_design = %s
        """,
        (id_design,)
    )
    tags = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    tags = [dict(zip(columns, row)) for row in tags]
    db.close_connection()
    return tags


# designs
def set_design(design: Design, list_of_tags_ids: list[int]):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO designs (name, img_url, ai_url) VALUES (%s, %s, %s)",
        (design.name, design.img_url, design.ai_url)
    )
    db.get_connection().commit()
    design.id_design = cursor.lastrowid
    
    for tag_id in list_of_tags_ids:
        cursor.execute(
            "INSERT INTO tag_design (id_tag, id_design) VALUES (%s, %s)",
            (tag_id, design.id_design)
        )
    db.get_connection().commit()
    db.close_connection()

def get_designs(google_sub: str = None):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM designs")
    designs = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    designs = [dict(zip(columns, row)) for row in designs]
    for design in designs:
        design["tags"] = get_tags_by_design_id(design["id"])
        
    if google_sub is not None:
        # if the google sub is provided, get the favorite designs and the cart designs
        pass
        
    db.close_connection()
    return designs

def get_design_by_id(id_design: int, google_sub: str = None):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "SELECT * FROM designs WHERE id = %s",
        (id_design,)
    )
    design = cursor.fetchone()
    design_dict = dict(zip([column[0] for column in cursor.description], design))
    design_dict["tags"] = get_tags_by_design_id(id_design)
    
    if google_sub is not None:
        pass
    
    db.close_connection()
    return design_dict

def delete_design(id_design: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM designs WHERE id = %s",
        (id_design,)
    )
    db.get_connection().commit()
    db.close_connection()

def update_design(design: Design, list_of_tags_ids: list[int]):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE designs SET name = %s, img_url = %s, ai_url = %s WHERE id = %s",
        (design.name, design.img_url, design.ai_url, design.id_design)
    )
    db.get_connection().commit()
    
    cursor.execute(
        "DELETE FROM tag_design WHERE id_design = %s",
        (design.id_design,)
    )
    db.get_connection().commit()
    
    for tag_id in list_of_tags_ids:
        cursor.execute(
            "INSERT INTO tag_design (id_tag, id_design) VALUES (%s, %s)",
            (tag_id, design.id_design)
        )
    db.get_connection().commit()
    db.close_connection()


# users
def get_users():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    users = [dict(zip(columns, row)) for row in users]
    db.close_connection()
    return users

def delete_user(google_sub: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM users WHERE google_sub = %s",
        (google_sub,)
    )
    db.get_connection().commit()
    db.close_connection()

def update_user(user: User):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE users SET name = %s, email = %s, phone = %s, img_url = %s WHERE google_sub = %s",
        (user.name, user.email, user.phone, user.img_url, user.google_sub)
    )
    db.get_connection().commit()
    db.close_connection()

def set_new_user(user: User):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO users (google_sub, name, email, phone, img_url) VALUES (%s, %s, %s, %s, %s)",
        (user.google_sub, user.name, user.email, user.phone, user.img_url)
    )
    db.get_connection().commit()
    db.close_connection()


# extra info
def set_extra_info(name: str, value: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO extra_info (name, value) VALUES (%s, %s)",
        (name, value)
    )
    db.get_connection().commit()
    db.close_connection()

def get_extra_info(name: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "SELECT * FROM extra_info WHERE name = %s",
        (name,)
    )
    extra_info = cursor.fetchone()
    extra_info = dict(zip([column[0] for column in cursor.description], extra_info))
    db.close_connection()
    return extra_info

def get_all_extra_info():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM extra_info")
    extra_info = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    extra_info = [dict(zip(columns, row)) for row in extra_info]
    db.close_connection()
    return extra_info

def update_extra_info(name: str, value: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE extra_info SET value = %s WHERE name = %s",
        (value, name)
    )
    db.get_connection().commit()
    db.close_connection()

def delete_extra_info(name: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM extra_info WHERE name = %s",
        (name,)
    )
    db.get_connection().commit()
    db.close_connection()


# favorite designs
def add_design_to_favorite(user_sub: str, design_id: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """
        INSERT INTO favorite_list_design (id_user, id_designs)
        SELECT %s, %s
        WHERE NOT EXISTS (
            SELECT 1 FROM favorite_list_design WHERE id_user = %s AND id_designs = %s
        )
        """,
        (user_sub, design_id, user_sub, design_id)
    )
    db.get_connection().commit()
    db.close_connection()

def remove_design_from_favorite(user_sub: str, design_id: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM favorite_list_design WHERE id_user = %s AND id_designs = %s",
        (user_sub, design_id)
    )
    db.get_connection().commit()
    db.close_connection()

def get_favorite_designs(user_sub: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """
        SELECT designs.*
        FROM favorite_list_design
        JOIN designs ON favorite_list_design.id_designs = designs.id
        WHERE favorite_list_design.id_user = %s
        """,
        (user_sub,)
    )
    designs = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    designs = [dict(zip(columns, row)) for row in designs]
    db.close_connection()
    return designs


# cart designs
def add_design_to_cart(user_sub: str, design_id: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """
        INSERT INTO cart_design (id_user, id_designs)
        SELECT %s, %s
        WHERE NOT EXISTS (
            SELECT 1 FROM cart_design WHERE id_user = %s AND id_designs = %s
        )
        """,
        (user_sub, design_id, user_sub, design_id)
    )
    db.get_connection().commit()
    db.close_connection()

def remove_design_from_cart(user_sub: str, design_id: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM cart_design WHERE id_user = %s AND id_designs = %s",
        (user_sub, design_id)
    )
    db.get_connection().commit()
    db.close_connection()

def get_cart_designs(user_sub: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """
        SELECT designs.*
        FROM cart_design
        JOIN designs ON cart_design.id_designs = designs.id
        WHERE cart_design.id_user = %s
        """,
        (user_sub,)
    )
    designs = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    designs = [dict(zip(columns, row)) for row in designs]
    db.close_connection()
    return designs


# phone number
def add_or_reset_number_to_user(google_sub: str, number: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE users SET phone = %s WHERE google_sub = %s",
        (number, google_sub)
    )
    db.get_connection().commit()
    db.close_connection()

def delete_number_to_user(google_sub: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE users SET phone = NULL WHERE google_sub = %s",
        (google_sub,)
    )
    db.get_connection().commit()
    db.close_connection()