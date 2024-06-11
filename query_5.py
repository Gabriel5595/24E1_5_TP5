import sqlite3

def query_5():
  print()
  print("*** QUERY 5 ***")
  print("Mostrar todos os Metadados por evento.")
  print()
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()

  cursor.execute("""SELECT NOME,
                            METADADO
                    FROM EVENTOS
                    JOIN METADADOS ON EVENTOS.METADADO_ID = METADADOS.METADADO_ID""")

  results = cursor.fetchall()
  for line in results:
      print(line)

  conn.close()