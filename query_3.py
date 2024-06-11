import sqlite3

def query_3():
    print()
    print("*** QUERY 3 ***")
    print("Mostrar os eventos que acontecem no Rio de Janeiro.")
    print()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT NOME,
                            LOCALIZACAO
                    FROM EVENTOS
                    JOIN DADOS_EVENTOS ON EVENTOS.DADO_ID = DADOS_EVENTOS.DADO_ID
                    WHERE LOCALIZACAO = 'Rio de Janeiro/RJ'""")
                    

    results = cursor.fetchall()
    
    if results == []:
        print("Nenhum evento agendado.")
    else:
        for line in results:
            print(line)
        
    
    conn.close()