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
                host=os.getenv("PG_HOST"),
                dbname=os.getenv("PG_DBNAME"),
                user=os.getenv("PG_USER"),
                password=os.getenv("PG_PASSWORD")
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
        
    def export_db(self, filename):
        try:
            cursor = self.get_cursor()
            
            # Obtener todas las tablas
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
            tables = cursor.fetchall()

            with open(filename, 'w') as f:
                for table in tables:
                    table_name = table[0]

                    # Obtener el esquema de la tabla
                    cursor.execute(f"SELECT column_name, data_type, character_maximum_length FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table_name}'")
                    columns = cursor.fetchall()
                    create_table = f"CREATE TABLE {table_name} (\n"
                    create_table += ",\n".join([f"{col[0]} {col[1]}{f'({col[2]})' if col[2] else ''}" for col in columns])
                    create_table += "\n);\n\n"
                    f.write(create_table)

                    # Obtener los datos de la tabla
                    cursor.execute(f"SELECT * FROM {table_name}")
                    rows = cursor.fetchall()
                    for row in rows:
                        insert_row = f"INSERT INTO {table_name} VALUES ({', '.join([repr(val) for val in row])});\n"
                        f.write(insert_row)
                    f.write("\n")
            
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