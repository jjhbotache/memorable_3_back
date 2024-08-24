import os
import psycopg2
import threading
import dotenv
import re
dotenv.load_dotenv()

class DatabaseConnection:
    _instance = None
    _connection_holder = threading.local()
    
    create_tables_sql = """
CREATE TABLE IF NOT EXISTS users (
    google_sub TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    img_url TEXT
);

CREATE TABLE IF NOT EXISTS designs (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    img_url TEXT,
    ai_url TEXT
);

CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cart_design (
    id SERIAL PRIMARY KEY,
    id_user TEXT,
    id_designs INTEGER,
    FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
    FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS favorite_list_design (
    id SERIAL PRIMARY KEY,
    id_user TEXT,
    id_designs INTEGER,
    FOREIGN KEY (id_user) REFERENCES users(google_sub) ON DELETE CASCADE,
    FOREIGN KEY (id_designs) REFERENCES designs(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tag_design (
    id SERIAL PRIMARY KEY,
    id_tag INTEGER,
    id_design INTEGER,
    FOREIGN KEY (id_tag) REFERENCES tags(id) ON DELETE CASCADE,
    FOREIGN KEY (id_design) REFERENCES designs(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS extra_info (
    name TEXT NOT NULL,
    value TEXT
);

        """


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_connection(self):
        if not hasattr(self._connection_holder, "connection"):
            self._connection_holder.connection = psycopg2.connect(os.getenv("PG_URL"))
            
        return self._connection_holder.connection

    def get_cursor(self):
        try:
            connection = self.get_connection()
            return connection.cursor()
        except Exception as e:
            print(f"Error al obtener el cursor: {e}")
            # retry
            self.close_connection()
            return self.get_cursor()
        
    
    def close_connection(self):
        if hasattr(self._connection_holder, "connection"):
            self._connection_holder.connection.close()
            del self._connection_holder.connection
        
    def create_tables(self):
        cursor = self.get_cursor()
        
        cursor.execute(DatabaseConnection.create_tables_sql)
        self.get_connection().commit()
        
    def export_db(self, filename):
        try:
            cursor = self.get_cursor()
            
            # Obtener todas las tablas
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
            tables = cursor.fetchall()
    
            export_sql = DatabaseConnection.create_tables_sql + "\n"
    
            # Expresión regular para encontrar los nombres de las tablas
            table_name_pattern = re.compile(r'CREATE TABLE IF NOT EXISTS (\w+)')
            
            # Buscar todos los nombres de las tablas
            table_names = table_name_pattern.findall(DatabaseConnection.create_tables_sql)
            
    
            for table_name in table_names:
    
    
                # Obtener los datos de la tabla
                cursor.execute(f"SELECT * FROM {table_name}")
                rows = cursor.fetchall()
                for row in rows:
                    insert_row = f"""INSERT INTO {table_name} VALUES ({', '.join(
                        [ "'"+val.replace("'","''")+"'" if isinstance(val, str) else str(val).replace('None', 'NULL')
                        for val in row]
                        )});\n"""
                    export_sql += insert_row
                export_sql += "\n"
    
            with open(filename, 'w') as f:
                f.write(export_sql)
            
            cursor.close()
            self.close_connection()
            print(f"Base de datos exportada como {filename}")
        except Exception as e:
            print(f"Error al exportar la base de datos: {e}")

    def import_db(self, filename):
        try:
            cursor = self.get_cursor()
            
            # Clean the database by dropping all tables
            cursor.execute("""
                DO $$ DECLARE
                    r RECORD;
                BEGIN
                    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
                        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                    END LOOP;
                END $$;
            """)
            self.get_connection().commit()

            # Import the new database
            with open(filename, 'r') as f:
                sql = f.read()
                cursor.execute(sql)
            
            self.get_connection().commit()
            print(f"Base de datos importada desde {filename}")
        except Exception as e:
            print(f"Error al importar la base de datos: {e}")
        finally:
            cursor.close()
            self.close_connection()