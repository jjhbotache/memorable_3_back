import sqlite3
import threading

class DatabaseConnection:
    _instance = None
    database_name = 'data.db'
    _connection_holder = threading.local()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_connection(self):
        if not hasattr(self._connection_holder, "connection"):
            self._connection_holder.connection = sqlite3.connect(self.database_name, check_same_thread=False)
        return self._connection_holder.connection

    def get_cursor(self):
        connection = self.get_connection()
        return connection.cursor()
    
    def close_connection(self):
        if hasattr(self._connection_holder, "connection"):
            self._connection_holder.connection.close()
            del self._connection_holder.connection
        
    def create_tables(self):
    # create the tables
        self.get_cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                google_sub TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                img_url TEXT
            );
        """)
        self.get_cursor.execute("""
            CREATE TABLE IF NOT EXISTS designs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                img_url TEXT,
                ai_url TEXT
            );
        """)
        self.get_cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)
        self.get_cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
        self.get_cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorite_list_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
        self.get_cursor.execute("""
            CREATE TABLE IF NOT EXISTS tag_design (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_tag INTEGER,
                id_design INTEGER,
                FOREIGN KEY (id_tag) REFERENCES tags(id) ON DELETE CASCADE,
                FOREIGN KEY (id_design) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
    
