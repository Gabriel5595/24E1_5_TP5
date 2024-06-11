from drop_tables import drop_tables
from find_data import find_data
from generate_csv import generate_csv
from create_table_DADOS_EVENTOS import create_table_DADOS_EVENTOS
from create_table_EVENTOS import create_table_EVENTOS
from create_table_METADADOS import create_table_METADADOS
from consistency_test import consistency_test
from populate_table_DADOS_EVENTOS import populate_table_DADOS_EVENTOS
from populate_table_EVENTOS import populate_table_EVENTOS
from populate_table_METADADOS import populate_table_METADADOS
from query_1 import query_1
from query_2 import query_2
from query_3 import query_3
from query_4 import query_4
from query_5 import query_5
from type_refinament import type_refinament

def main():
  data = find_data()
  generate_csv(data)

  print("\nData retrival done")

  print("\nInitiating table creation...")

  drop_tables()
  
  create_table_DADOS_EVENTOS()
  create_table_METADADOS()
  create_table_EVENTOS()

  populate_table_DADOS_EVENTOS(data)
  populate_table_METADADOS(data)
  populate_table_EVENTOS(data)

  print("\nTable creation done.")

  #consistency_test()
  
  query_1()
  query_2()
  query_3()
  query_4()
  query_5()
  
  

main()