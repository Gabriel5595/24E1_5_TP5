import sqlite3

def query_4():
    print()
    print("*** QUERY 4 ***")
    print("Mostrar todos os eventos que são ao ar livre.")
    print()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT NOME,
                            TIPO
                    FROM EVENTOS
                    JOIN DADOS_EVENTOS ON EVENTOS.DADO_ID = DADOS_EVENTOS.DADO_ID
                    WHERE TIPO = 'Ar Livre'""")


    results = cursor.fetchall()

    if results == []:
        print("Nenhum evento agendado.")
    else:
        for line in results:
            print(line)


    conn.close()