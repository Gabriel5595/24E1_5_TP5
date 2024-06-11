import pandas as pd

def generate_csv(data):
  df = pd.DataFrame(data)
  df.to_csv('files/eventos.csv', index=False)