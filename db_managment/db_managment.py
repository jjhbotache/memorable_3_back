from classes.user import User
from classes.design import Design
from classes.tag import Tag
from classes.databaseConnection import execute_query, fetch_query, local_db_name

def get_user_by_google_sub(google_sub: str):
    query = f"SELECT * FROM users WHERE google_sub = '{google_sub}'"
    user = fetch_query(query)
    return user[0] if user else None

def get_img_urls():
    query = "SELECT img_url FROM designs"
    img_urls = fetch_query(query)
    return img_urls

def set_tag(tag: Tag):
    query = f"INSERT INTO tags (name) VALUES ('{tag.name}')"
    execute_query(query)
    tag.id_tag = fetch_query("SELECT last_insert_rowid()")[0][0]
    return tag

def get_tags_from_db():
    query = "SELECT * FROM tags"
    tags = fetch_query(query)
    columns = ["id", "name"]
    tags = [dict(zip(columns, row)) for row in tags]
    return tags

def update_tag_in_db(tag: Tag):
    query = f"UPDATE tags SET name = '{tag.name}' WHERE id = {tag.id_tag}"
    execute_query(query)

def delete_tag(tag: Tag):
    query = f"DELETE FROM tags WHERE id = {tag.id_tag}"
    execute_query(query)

def get_tags_by_design_id(id_design: int):
    query = f"""
        SELECT tags.id, tags.name
        FROM tag_design 
        JOIN tags ON tag_design.id_tag = tags.id
        WHERE tag_design.id_design = {id_design}
    """
    tags = fetch_query(query)
    columns = ["id", "name"]
    tags = [dict(zip(columns, row)) for row in tags]
    return tags

def set_design(design: Design, list_of_tags_ids: list[int]):
    query = f"INSERT INTO designs (name, img_url, ai_url) VALUES ('{design.name}', '{design.img_url}', '{design.ai_url}')"
    execute_query(query)
    design.id_design = fetch_query("SELECT last_insert_rowid()")[0][0]
    for tag_id in list_of_tags_ids:
        query = f"INSERT INTO tag_design (id_tag, id_design) VALUES ({tag_id}, {design.id_design})"
        execute_query(query)

def get_designs(google_sub: str = None):
    query = "SELECT * FROM designs"
    designs = fetch_query(query)
    columns = ["id", "name", "img_url", "ai_url"]
    designs = [dict(zip(columns, row)) for row in designs]
    return designs

def get_design_by_id(id_design: int, google_sub: str = None):
    query = f"SELECT * FROM designs WHERE id = {id_design}"
    design = fetch_query(query)
    if design:
        design_dict = dict(zip(["id", "name", "img_url", "ai_url"], design[0]))
        design_dict["tags"] = get_tags_by_design_id(id_design)
        return design_dict
    return None

def delete_design(id_design: int):
    query = f"DELETE FROM designs WHERE id = {id_design}"
    execute_query(query)

def update_design(design: Design, list_of_tags_ids: list[int]):
    query = f"UPDATE designs SET name = '{design.name}', img_url = '{design.img_url}', ai_url = '{design.ai_url}' WHERE id = {design.id_design}"
    execute_query(query)
    query = f"DELETE FROM tag_design WHERE id_design = {design.id_design}"
    execute_query(query)
    for tag_id in list_of_tags_ids:
        query = f"INSERT INTO tag_design (id_tag, id_design) VALUES ({tag_id}, {design.id_design})"
        execute_query(query)

def get_users():
    query = "SELECT * FROM users"
    users = fetch_query(query)
    columns = ["google_sub", "name", "email", "phone", "img_url"]
    users = [dict(zip(columns, row)) for row in users]
    return users

def delete_user(google_sub: str):
    query = f"DELETE FROM users WHERE google_sub = '{google_sub}'"
    execute_query(query)

def update_user(user: User):
    query = f"UPDATE users SET name = '{user.name}', email = '{user.email}', phone = '{user.phone}', img_url = '{user.img_url}' WHERE google_sub = '{user.google_sub}'"
    execute_query(query)

def set_new_user(user: User):
    query = f"INSERT INTO users (google_sub, name, email, phone, img_url) VALUES ('{user.google_sub}', '{user.name}', '{user.email}', '{user.phone}', '{user.img_url}')"
    execute_query(query)

def import_db(source_path: str, destination_path: str):
    try:
        with open(source_path, 'rb') as f_src, open(destination_path, 'wb') as f_dst:
            f_dst.write(f_src.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def export_db(source_path: str, destination_path: str):
    try:
        with open(source_path, 'rb') as f_src, open(destination_path, 'wb') as f_dst:
            f_dst.write(f_src.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_or_reset_number_to_user(google_sub: str, number: str):
    query = f"UPDATE users SET phone = '{number}' WHERE google_sub = '{google_sub}'"
    execute_query(query)

def delete_number_to_user(google_sub: str):
    query = f"UPDATE users SET phone = NULL WHERE google_sub = '{google_sub}'"
    execute_query(query)

def add_design_to_favorite(user_sub: str, design_id: int):
    query = f"INSERT INTO favorite_list_design (id_user, id_designs) VALUES ('{user_sub}', {design_id})"
    execute_query(query)

def remove_design_from_favorite(user_sub: str, design_id: int):
    query = f"DELETE FROM favorite_list_design WHERE id_user = '{user_sub}' AND id_designs = {design_id}"
    execute_query(query)

def get_favorite_designs(user_sub: str):
    query = f"SELECT * FROM favorite_list_design WHERE id_user = '{user_sub}'"
    favorite_designs = fetch_query(query)
    columns = ["id", "id_user", "id_designs"]
    favorite_designs = [dict(zip(columns, row)) for row in favorite_designs]
    return favorite_designs

def add_design_to_cart(user_sub: str, design_id: int):
    query = f"INSERT INTO cart_design (id_user, id_designs) VALUES ('{user_sub}', {design_id})"
    execute_query(query)

def remove_design_from_cart(user_sub: str, design_id: int):
    query = f"DELETE FROM cart_design WHERE id_user = '{user_sub}' AND id_designs = {design_id}"
    execute_query(query)

def get_cart_designs(user_sub: str):
    query = f"SELECT * FROM cart_design WHERE id_user = '{user_sub}'"
    cart_designs = fetch_query(query)
    columns = ["id", "id_user", "id_designs"]
    cart_designs = [dict(zip(columns, row)) for row in cart_designs]
    return cart_designs

def set_extra_info(name: str, value: str):
    query = f"INSERT INTO extra_info (name, value) VALUES ('{name}', '{value}')"
    execute_query(query)

def get_extra_info(name: str):
    query = f"SELECT * FROM extra_info WHERE name = '{name}'"
    extra_info = fetch_query(query)
    return extra_info[0] if extra_info else None

def get_all_extra_info():
    query = "SELECT * FROM extra_info"
    extra_info = fetch_query(query)
    columns = ["name", "value"]
    extra_info = [dict(zip(columns, row)) for row in extra_info]
    return extra_info

def update_extra_info(name: str, value: str):
    query = f"UPDATE extra_info SET value = '{value}' WHERE name = '{name}'"
    execute_query(query)

def delete_extra_info(name: str):
    query = f"DELETE FROM extra_info WHERE name = '{name}'"
    execute_query(query)