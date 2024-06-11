import sqlite3

def consistency_test():

    print("\nInitiating consistency test...\n")

    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()

        print("\n*** TABLE EVENTOS ***")
        cursor.execute("SELECT * FROM EVENTOS")
        results = cursor.fetchall()
        for line in results:
          print(line)

        print("\n*** TABLE DADOS_EVENTOS ***")
        cursor.execute("SELECT * FROM DADOS_EVENTOS")
        results = cursor.fetchall()
        for line in results:
          print(line)
        
        print("\n*** TABLE METADADOS ***")
        cursor.execute("SELECT * FROM METADADOS")
        results = cursor.fetchall()
        for line in results:
          print(line)