import sqlite3

from type_refinament import type_refinament

def populate_table_EVENTOS(events_info):

    with sqlite3.connect("database.db", timeout=60) as connection:
        cursor = connection.cursor()


    for i, event in enumerate(events_info):
        cursor.execute("""INSERT INTO EVENTOS (DADO_ID, METADADO_ID, NOME, TIPO) VALUES (?, ?, ?, ?)""", (i, 1, event["title"], event["type"]))

    connection.commit()
    cursor.close()

    type_refinament()

    print('\nValues inserted successfully!')