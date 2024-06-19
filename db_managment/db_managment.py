from classes.user import User
from classes.databaseConnection import DatabaseConnection
from classes.design import Design
from classes.tag import Tag
import shutil


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


    
def get_img_urls():
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute( "SELECT img_url FROM designs" )
    img_urls = cursor.fetchall()
    db.connection.close()
    return img_urls

    
    
# tags
def set_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "INSERT INTO tags (name) VALUES (?)",
        (tag.name,)
    )
    db.connection.commit()
    db.connection.close()
    # update the tag id and return it
    tag.id_tag = cursor.lastrowid
    return tag

def get_tags_from_db():
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute("SELECT * FROM tags")
    tags = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    tags = [dict(zip(columns, row)) for row in tags]
    db.connection.close()
    
    # return tags
    return tags

def update_tag_in_db(tag: Tag):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "UPDATE tags SET name = ? WHERE id = ?",
        (tag.name, tag.id_tag)
    )
    db.connection.commit()
    db.connection.close()
    
def delete_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "DELETE FROM tags WHERE id = ?",
        (tag.id_tag,)
    )
    db.connection.commit()
    db.connection.close()
    
def get_tags_by_design_id(id_design:int):
    db = DatabaseConnection()
    cursor = db.cursor
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
    
    
    
    db.connection.close()
    return tags
    
# designs
def set_design(design: Design, list_of_tags_ids: list[int]):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "INSERT INTO designs (name, img_url, ai_url) VALUES (?, ?, ?)",
        (design.name, design.img_url, design.ai_url)
    )
    db.connection.commit()
    design.id_design = cursor.lastrowid
    
    # set the tags related to the design
    
    for tag_id in list_of_tags_ids:
        cursor.execute(
            "INSERT INTO tag_design (id_tag,id_design) VALUES (?, ?)",
            (tag_id, design.id_design)
        )
    db.connection.commit()
    db.connection.close()

def get_designs():
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute("SELECT * FROM designs")
    designs = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    designs = [dict(zip(columns, row)) for row in designs]
    for design in designs:
        design["tags"] = get_tags_by_design_id(design["id"])
        
    db.connection.close()
    
    return designs

def get_design_by_id(id_design:int):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "SELECT * FROM designs WHERE id = ?",
        (id_design,)
    )
    design = cursor.fetchone()
    # return a dict with the data
    design_dict = dict(zip([column[0] for column in cursor.description], design))
    # get also the tags
    design_dict["tags"] = get_tags_by_design_id(id_design)
    
    db.connection.close()
    return design_dict

def delete_design(id_design:int):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "DELETE FROM designs WHERE id = ?",
        (id_design,)
    )
    db.connection.commit()
    db.connection.close()
    
def update_design(design:Design, list_of_tags_ids:list[int]):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "UPDATE designs SET name = ?, img_url = ?, ai_url = ? WHERE id = ?",
        (design.name, design.img_url, design.ai_url, design.id_design)
    )
    db.connection.commit()
    
    # delete the old tags
    cursor.execute(
        "DELETE FROM tag_design WHERE id_design = ?",
        (design.id_design,)
    )
    db.connection.commit()
    
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
        
    
    db.connection.commit()
    db.connection.close()
    
#users
def get_users():
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    users = [dict(zip(columns, row)) for row in users]
    db.connection.close()
    return users

def delete_user(google_sub:str):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "DELETE FROM users WHERE google_sub = ?",
        (google_sub,)
    )
    db.connection.commit()
    db.connection.close()
    
def update_user(user:User):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "UPDATE users SET name = ?, email = ?, phone = ?, img_url = ? WHERE google_sub = ?",
        (user.name, user.email, user.phone, user.img_url, user.google_sub)
    )
    db.connection.commit()
    db.connection.close()
    
def set_new_user(user:User):
    connection = DatabaseConnection()
    connection.cursor.execute(
        "INSERT INTO users (google_sub, name, email, phone, img_url) VALUES (?, ?, ?, ?, ?)",
        (user.google_sub, user.name, user.email, user.phone, user.img_url)
    )
    connection.connection.commit()
    connection.connection.close()
    
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