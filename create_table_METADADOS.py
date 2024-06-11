import sqlite3

def create_table_METADADOS():
  with sqlite3.connect("database.db", timeout=60) as connection:
    cursor = connection.cursor()

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS METADADOS(
        METADADO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        METADADO VARCHAR(255) NOT NULL    
    )
  """)
  connection.commit()
  cursor.close()

  print("\nTable created sucessfully!")