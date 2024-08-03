import os
import psycopg2
import threading

class DatabaseConnection:
    _instance = None
    _connection_holder = threading.local()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_connection(self):
        if not hasattr(self._connection_holder, "connection"):
            self._connection_holder.connection = psycopg2.connect(
                host=os.getenv("PG_HOST", "dpg-cqmro6lsvqrc73femdb0-a.oregon-postgres.render.com"),
                dbname=os.getenv("PG_DBNAME", "memorable_db_tmxo"),
                user=os.getenv("PG_USER", "juan"),
                password=os.getenv("PG_PASSWORD", "AwGtkXpRBKYwpJRNhkHDMfsG7tbBzb8T")
            )
            
        return self._connection_holder.connection

    def get_cursor(self):
        connection = self.get_connection()
        return connection.cursor()
    
    def close_connection(self):
        if hasattr(self._connection_holder, "connection"):
            self._connection_holder.connection.close()
            del self._connection_holder.connection
        
    def create_tables(self):
        cursor = self.get_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                google_sub TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                img_url TEXT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS designs (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                img_url TEXT,
                ai_url TEXT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart_design (
                id SERIAL PRIMARY KEY,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
        cursor.execute("""
            ALTER TABLE cart_design
            ADD CONSTRAINT fk_cart_design_users
            FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE;
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorite_list_design (
                id SERIAL PRIMARY KEY,
                id_user TEXT,
                id_designs INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
                FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tag_design (
                id SERIAL PRIMARY KEY,
                id_tag INTEGER,
                id_design INTEGER,
                FOREIGN KEY (id_tag) REFERENCES tags(id) ON DELETE CASCADE,
                FOREIGN KEY (id_design) REFERENCES designs(id) ON DELETE CASCADE
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS extra_info (
                name TEXT NOT NULL,
                value TEXT
            );
        """)
        self.get_connection().commit()