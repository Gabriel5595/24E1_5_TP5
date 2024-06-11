from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

from format_date import format_date

def find_data():
  url = "https://www.turismo.gov.br/agenda-eventos/views/calendario.php"
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

  req = Request(url, headers=headers)
  try:
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    titles = soup.find_all("span", class_="nome")
    dates_day = soup.find_all("span", class_="dia")
    dates_month = soup.find_all("span", class_="mes")
    locations = soup.find_all("span", class_="localizacao mt")
    metadata = soup.find("meta", attrs={'name': 'viewport'})
    types = []
    types.extend(soup.find_all("div", class_="categoria acontecendo"))
    types.extend(soup.find_all("div", class_="categoria trintadias"))
    types.extend(soup.find_all("div", class_="categoria sessentadias"))
    types.extend(soup.find_all("div", class_="categoria noventadias"))
    types.extend(soup.find_all("div", class_="categoria noventadiasmais"))
    
    events_info = []

    if len(titles) == len(dates_day) == len(dates_month) == len(types) == len(locations):

      viewport_content = metadata['content'] if metadata and metadata.has_attr('content') else None

      for id, (title, date_day, date_month, type, location) in enumerate(zip(titles, dates_day, dates_month, types, locations), start=1):
        
        day = date_day.get_text(strip=True)
        month = date_month.get_text(strip=True)

        events_info.append({
          "id": id,
          "title": title.get_text(strip=True),
          "date": format_date(day, month),
          "type": type.get_text(strip=True),
          "location": location.get_text(strip=True),
          "metadata": viewport_content
        })

    else:
      print("O número de títulos e descrições não corresponde.")

    #for event in events_info:
    #  print(f"ID: {event['id' ]}, Título: {event['title']}, Data: {event['date']}")

    return events_info

  except HTTPError as e:
      print(f"HTTP error: {e.reason}")
  except URLError as e:
      print(f"URL error: {e.reason}")