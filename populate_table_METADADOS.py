import sqlite3

def populate_table_METADADOS(events_info):

    metadado = events_info[0]["metadata"]

    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()

        cursor.execute("""INSERT INTO METADADOS (METADADO) VALUES (?)""", (metadado,))

    connection.commit()
    cursor.close()

    print('\nValues inserted successfully!')