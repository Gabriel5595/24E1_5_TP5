import datetime

def format_date(day, month):
  month_mapping = {
      "Jan": "01",
      "Fev": "02",
      "Mar": "03",
      "Abr": "04",
      "Mai": "05",
      "Jun": "06",
      "Jul": "07",
      "Ago": "08",
      "Set": "09",
      "Out": "10",
      "Nov": "11",
      "Dez": "12"
  }
  
  year = datetime.datetime.now().year
  month_number = month_mapping[month]
  # Formatar a data no formato 'YYYY-MM-DD'
  date_str = f"{year}-{month_number}-{day.zfill(2)}"
  return date_str