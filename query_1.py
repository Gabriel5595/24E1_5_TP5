import sqlite3

def query_1():
  print()
  print("*** QUERY 1 ***")
  print("Mostrar todos os eventos com suas datas, localização, e tipo de evento.")
  print()
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()

  cursor.execute("""SELECT NOME,
                            DATA,
                            LOCALIZACAO
                    FROM EVENTOS
                    JOIN DADOS_EVENTOS ON EVENTOS.DADO_ID = DADOS_EVENTOS.DADO_ID
                    JOIN METADADOS ON EVENTOS.METADADO_ID = METADADOS.METADADO_ID""")

  results = cursor.fetchall()
  for line in results:
      print(line)
  
  conn.close()