import sqlite3

def create_table_EVENTOS():
  with sqlite3.connect("database.db", timeout=60) as connection:
    cursor = connection.cursor()

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS EVENTOS(
        EVENTO_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DADO_ID INT NOT NULL,
        METADADO_ID INT NOT NULL,
        NOME VARCHAR(255) NOT NULL,
        TIPO VARCHAR(255) NOT NULL,
        FOREIGN KEY (DADO_ID) REFERENCES DADOS_EVENTOS(DADO_ID),
        FOREIGN KEY (METADADO_ID) REFERENCES METADADOS(METADADO_ID)
    )
  """)
  connection.commit()
  cursor.close()

  print("\nTable created sucessfully!")