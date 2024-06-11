import sqlite3

from modify_type import modify_type

def type_refinament():    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT EVENTO_ID, TIPO FROM EVENTOS")
    
    linhas = cursor.fetchall()

    for linha in linhas:
        EVENTO_ID, tipo_atual = linha
        novo_tipo = modify_type(tipo_atual)

        if tipo_atual != novo_tipo:
            cursor.execute("UPDATE EVENTOS SET tipo = ? WHERE EVENTO_ID = ?", (novo_tipo, EVENTO_ID))

    conn.commit()
    conn.close()