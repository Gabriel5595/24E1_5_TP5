import sqlite3

def create_table_DADOS_EVENTOS():
  with sqlite3.connect("database.db", timeout=60) as connection:
    cursor = connection.cursor()

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS DADOS_EVENTOS(
        DADO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DATA DATE NOT NULL,
        LOCALIZACAO VARCHAR(255) NOT NULL
    )
  """)
  connection.commit()
  cursor.close()

  print("\nTable created sucessfully!")