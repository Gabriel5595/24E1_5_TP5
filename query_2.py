import sqlite3

def query_2():
  print()
  print("*** QUERY 2 ***")
  print("Mostrar os dados dos 2 eventos mais próximos de iniciar.")
  print()
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()

  cursor.execute("""SELECT NOME,
                            DATA
                    FROM EVENTOS
                    JOIN DADOS_EVENTOS ON EVENTOS.DADO_ID = DADOS_EVENTOS.DADO_ID
                    ORDER BY DATA ASC
                    LIMIT 2""")

  results = cursor.fetchall()
  for line in results:
      print(line)

  conn.close()