import sqlite3

def drop_tables():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS DADOS_EVENTOS;
""")

    cursor.execute("""
        DROP TABLE IF EXISTS METADADOS;
""")

    cursor.execute("""
        DROP TABLE IF EXISTS EVENTOS;
""")

    connection.commit()

    print("\nTables dropped sucessfully!")