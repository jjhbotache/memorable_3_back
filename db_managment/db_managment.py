from classes.user import User
from classes.databaseConnection import DatabaseConnection
from classes.design import Design
from classes.tag import Tag


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
        "INSERT INTO users (google_sub, name, email, phone, img_url) VALUES (?, ?, ?, ?, ?)",
        (user.google_sub, user.name, user.email, user.phone, user.img_url)
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

def get_tags():
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute("SELECT * FROM tags")
    tags = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    tags = [dict(zip(columns, row)) for row in tags]
    db.connection.close()
    
    # return tags
    return tags

def update_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "UPDATE tags SET name = ? WHERE id_tag = ?",
        (tag.name, tag.id_tag)
    )
    db.connection.commit()
    db.connection.close()
    
def delete_tag(tag: Tag):
    db = DatabaseConnection()
    cursor = db.cursor
    cursor.execute(
        "DELETE FROM tags WHERE id_tag = ?",
        (tag.id_tag,)
    )
    db.connection.commit()
    db.connection.close()
    
    
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
    db.connection.close()
    
    # return designs
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