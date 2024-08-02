import sqlite3

def convert_db_to_sql(db_path: str, sql_path: str):
    try:
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Ejecutar el volcado de la base de datos en formato SQL
        with open(sql_path, 'w') as f:
            for line in conn.iterdump():
                f.write(f'{line}\n')
        
        print(f"Database exported to SQL file '{sql_path}' successfully.")
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    
    finally:
        if conn:
            conn.close()

# Ejemplo de uso:
convert_db_to_sql('local.db', 'dump.sql')
