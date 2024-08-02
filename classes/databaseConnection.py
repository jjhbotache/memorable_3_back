import libsql_experimental as libsql
from dotenv import load_dotenv
import os
load_dotenv()

turso_url = "libsql://memorabledb-jjhbotache.turso.io"

# Obtener el token de la variable de entorno
turso_token = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjI2NDA3MDcsImlkIjoiNjhhYzg3M2MtNmYxZC00OTU4LTg4ZTItNDdjNzliNmQwNGZiIn0.mxbmBDsiG7cjsvPRxbJBSMi8EefjccTI802B0BJ-e9f-wI3iO7icdaamF-qloMbAfdj7RNC33w8M6LPJWUJEBg"

local_db_name = "local.db"
conn = libsql.connect(local_db_name, sync_url=turso_url, auth_token=turso_token)
print("Connection established")
print(conn)
def create_tables():
        global conn
        # Users table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                google_sub TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                img_url TEXT
            )
        """)
        
        # Designs table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS designs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                img_url TEXT,
                ai_url TEXT
            )
        """)
        
        # Tags table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        
        # Cart design table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cart_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            )
        """)
        
        # Favorite list design table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS favorite_list_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            )
        """)
        
        # Tag design table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tag_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_tag INTEGER,
                id_design INTEGER,
                FOREIGN KEY (id_tag) REFERENCES tags(id) ON DELETE CASCADE,
                FOREIGN KEY (id_design) REFERENCES designs(id) ON DELETE CASCADE
            )
        """)
        
        # Extra info table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS extra_info (
                name TEXT NOT NULL,
                value TEXT
            )
        """)
        
        conn.commit()
        print("Tables created successfully")

def execute_query(query):
    conn.execute(query)
    conn.commit()
    
def fetch_query(query):
    cursor = conn.execute(query)
    return cursor.fetchall()

create_tables()