from classes.user import User
from classes.databaseConnection import DatabaseConnection
from classes.design import Design
from classes.tag import Tag
import shutil


def get_user_by_google_sub(google_sub:str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "SELECT * FROM users WHERE google_sub = ?",
        (google_sub,)
    )
    user = cursor.fetchone()
    db.close_connection()
    return user


    
def get_img_urls():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute( "SELECT img_url FROM designs" )
    img_urls = cursor.fetchall()
    db.close_connection()
    return img_urls

    
    
# tags
def set_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO tags (name) VALUES (?)",
        (tag.name,)
    )
    db.get_connection().commit()
    db.close_connection()
    # update the tag id and return it
    tag.id_tag = cursor.lastrowid
    return tag

def get_tags_from_db():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM tags")
    tags = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    tags = [dict(zip(columns, row)) for row in tags]
    db.close_connection()
    
    # return tags
    return tags

def update_tag_in_db(tag: Tag):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE tags SET name = ? WHERE id = ?",
        (tag.name, tag.id_tag)
    )
    db.get_connection().commit()
    db.close_connection()
    
def delete_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM tags WHERE id = ?",
        (tag.id_tag,)
    )
    db.get_connection().commit()
    db.close_connection()
    
def get_tags_by_design_id(id_design:int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """
        SELECT tags.id, tags.name
        FROM tag_design 
        JOIN tags ON tag_design.id_tag = tags.id
        WHERE tag_design.id_design = ?
        """,
        (id_design,)
    )
    tags = cursor.fetchall()
    # format the data to a list of dicts
    columns = [column[0] for column in cursor.description]
    tags = [dict(zip(columns, row)) for row in tags]
    
    
    
    db.close_connection()
    return tags
    
# designs
def set_design(design: Design, list_of_tags_ids: list[int]):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO designs (name, img_url, ai_url) VALUES (?, ?, ?)",
        (design.name, design.img_url, design.ai_url)
    )
    db.get_connection().commit()
    design.id_design = cursor.lastrowid
    
    # set the tags related to the design
    
    for tag_id in list_of_tags_ids:
        cursor.execute(
            "INSERT INTO tag_design (id_tag,id_design) VALUES (?, ?)",
            (tag_id, design.id_design)
        )
    db.get_connection().commit()
    db.close_connection()

def get_designs(google_sub:str):
    # if the user is not logged in, return all the designs
    
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM designs")
    designs = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    designs = [dict(zip(columns, row)) for row in designs]
    for design in designs:
        design["tags"] = get_tags_by_design_id(design["id"])
        
    if google_sub != None:
        # if the google sub is provided, get the favorite designs and the cart designs
        favorite_designs = get_favorite_designs(google_sub)
        cart_designs = get_cart_designs(google_sub)
        
        # for each design, if the id is in the favorite designs or in the cart designs, set the flag
        for design in designs:
            design["loved"] = design["id"] in [fav["id"] for fav in favorite_designs]
            design["addedToCart"] = design["id"] in [cart["id"] for cart in cart_designs]
            
        
    db.close_connection()
    
    return designs

def get_design_by_id(id_design:int, google_sub:str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "SELECT * FROM designs WHERE id = ?",
        (id_design,)
    )
    design = cursor.fetchone()
    # return a dict with the data
    design_dict = dict(zip([column[0] for column in cursor.description], design))
    # get also the tags
    design_dict["tags"] = get_tags_by_design_id(id_design)
    
    if(google_sub != None):
        # if the google sub is provided, get the favorite designs and the cart designs
        favorite_designs = get_favorite_designs(google_sub)
        cart_designs = get_cart_designs(google_sub)
        
        # set the flags
        design_dict["loved"] = design_dict["id"] in [fav["id"] for fav in favorite_designs]
        design_dict["addedToCart"] = design_dict["id"] in [cart["id"] for cart in cart_designs]
    
    db.close_connection()
    return design_dict

def delete_design(id_design:int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM designs WHERE id = ?",
        (id_design,)
    )
    db.get_connection().commit()
    db.close_connection()
    
def update_design(design:Design, list_of_tags_ids:list[int]):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE designs SET name = ?, img_url = ?, ai_url = ? WHERE id = ?",
        (design.name, design.img_url, design.ai_url, design.id_design)
    )
    db.get_connection().commit()
    
    # delete the old tags
    cursor.execute(
        "DELETE FROM tag_design WHERE id_design = ?",
        (design.id_design,)
    )
    db.get_connection().commit()
    
    # set the new tags
    if list_of_tags_ids == None or list_of_tags_ids == []:
        # clear the tags
        cursor.execute(
            "DELETE FROM tag_design WHERE id_design = ?",
            (design.id_design,)
        )
    else:
        for tag_id in list_of_tags_ids:
            cursor.execute(
                "INSERT INTO tag_design (id_tag,id_design) VALUES (?, ?)",
                (tag_id, design.id_design)
            )
        
    
    db.get_connection().commit()
    db.close_connection()
    
#users
def get_users():
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    users = [dict(zip(columns, row)) for row in users]
    db.close_connection()
    return users

def delete_user(google_sub:str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "DELETE FROM users WHERE google_sub = ?",
        (google_sub,)
    )
    db.get_connection().commit()
    db.close_connection()
    
def update_user(user:User):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        "UPDATE users SET name = ?, email = ?, phone = ?, img_url = ? WHERE google_sub = ?",
        (user.name, user.email, user.phone, user.img_url, user.google_sub)
    )
    db.get_connection().commit()
    db.close_connection()
    
def set_new_user(user:User):
    db = DatabaseConnection()
    db.get_cursor().execute(
        "INSERT INTO users (google_sub, name, email, phone, img_url) VALUES (?, ?, ?, ?, ?)",
        (user.google_sub, user.name, user.email, user.phone, user.img_url)
    )
    db.get_connection().commit()
    db.close_connection()
    
def import_db(source_path: str, destination_path: str):
    try:
        shutil.copyfile(source_path, destination_path)
        print("Database imported successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred during database import: {str(e)}")

def export_db(source_path: str, destination_path: str):
    try:
        shutil.copyfile(source_path, destination_path)
        print("Database exported successfully.")
    except FileNotFoundError:
        print("Destination directory not found.")
    except Exception as e:
        print(f"An error occurred during database export: {str(e)}")
        
 
 
# favorite designs crud
def add_design_to_favorite(user_sub: str, design_id: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    # if doesn't exist, add the user to the db
    
    cursor.execute(
        """
        INSERT INTO favorite_list_design (id_user, id_designs)
        SELECT ?, ?
        WHERE NOT EXISTS (
            SELECT 1 FROM favorite_list_design WHERE id_user = ? AND id_designs = ?
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
        """
        DELETE FROM favorite_list_design
        WHERE id_user = ? AND id_designs = ?
        """,
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
        WHERE favorite_list_design.id_user = ?
        """,
        (user_sub,)
    )
    designs = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    designs = [dict(zip(columns, row)) for row in designs]
    for design in designs: design["tags"] = get_tags_by_design_id(design["id"])
    db.close_connection()
    return designs

# cart designs crud
def add_design_to_cart(user_sub: str, design_id: int):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """
        INSERT INTO cart_design (id_user, id_designs)
        SELECT ?, ?
        WHERE NOT EXISTS (
            SELECT 1 FROM cart_design WHERE id_user = ? AND id_designs = ?
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
        """
        DELETE FROM cart_design
        WHERE id_user = ? AND id_designs = ?
        """,
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
        WHERE cart_design.id_user = ?
        """,
        (user_sub,)
    )
    designs = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    designs = [dict(zip(columns, row)) for row in designs]
    for design in designs: design["tags"] = get_tags_by_design_id(design["id"])
    db.close_connection()
    return designs


#extra info crud
def set_extra_info(name: str, value: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """INSERT INTO extra_info (name, value) VALUES (?, ?)""",
        (name, value)
    )
    db.get_connection().commit()
    db.close_connection()

def get_extra_info(name: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """SELECT * FROM extra_info WHERE name = ?""",
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
        """UPDATE extra_info SET value = ? WHERE name = ?""",
        (value, name)
    )
    db.get_connection().commit()
    db.close_connection()

def delete_extra_info(name: str):
    db = DatabaseConnection()
    cursor = db.get_cursor()
    cursor.execute(
        """DELETE FROM extra_info WHERE name = ?"""     ,
        (name,)
    )
    db.get_connection().commit()
    db.close_connection()
