import sqlite3

class DatabaseConnection:
    _instance = None
    database_name = 'data.db'
    
    def __new__(cls): # this method is called before __init__
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = sqlite3.connect(cls.database_name)
            
            
            
        return cls._instance
    
    def __init__(self):
        self.connection = sqlite3.connect(DatabaseConnection.database_name)
        self.cursor = self.connection.cursor()
        # create the tables
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                google_sub TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                image_url TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS designs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                image_url TEXT,
                ai_url TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                vector_url TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS carts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                FOREIGN KEY (id_user) REFERENCES users(google_sub)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cart INTEGER,
                id_designs INTEGER,
                FOREIGN KEY (id_cart) REFERENCES carts(id),
                FOREIGN KEY (id_designs) REFERENCES designs(id)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorite_lists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                FOREIGN KEY (id_user) REFERENCES users(google_sub)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorite_list_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_favorite_list INTEGER,
                id_designs INTEGER,
                FOREIGN KEY (id_favorite_list) REFERENCES favorite_lists(id),
                FOREIGN KEY (id_designs) REFERENCES designs(id)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tag_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_tag INTEGER,
                id_designs INTEGER,
                FOREIGN KEY (id_tag) REFERENCES tags(id),
                FOREIGN KEY (id_designs) REFERENCES designs(id)
            );
        """)
        

