import sqlite3

def populate_table_DADOS_EVENTOS(events_info):

    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()


    for event in events_info:
        cursor.execute("""INSERT INTO DADOS_EVENTOS (DATA, LOCALIZACAO) VALUES (?, ?)""", (event["date"], event["location"]))
        
    connection.commit()
    cursor.close()
        
    print('\nValues inserted successfully!')