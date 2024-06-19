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
        # if the file aleady exists, return
        self.connection = sqlite3.connect(DatabaseConnection.database_name)
        self.cursor = self.connection.cursor()
        
        # if the db is empty, create the tables
        self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        # if len(tables) == 0:
        self.create_tables()
        
    def create_tables(self):
    # create the tables
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                google_sub TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                img_url TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS designs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                img_url TEXT,
                ai_url TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorite_list_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tag_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_tag INTEGER,
                id_design INTEGER,
                FOREIGN KEY (id_tag) REFERENCES tags(id) ON DELETE CASCADE,
                FOREIGN KEY (id_design) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
    
