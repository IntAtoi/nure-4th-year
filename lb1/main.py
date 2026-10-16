import requests

url = "https://bank.gov.ua/NBU_Exchange/exchange_site"

params = {
    "start": "20260112",
    "end": "20260118",
    "valcode": "usd",
    "sort": "exchangedate",
    "order": "desc",
    "json": "",
}

response = requests.get(url, params=params)

if response.status_code == 200:
  data = response.json()
  for item in data:
    print(
        f"Дата: {item['exchangedate']} | Валюта: {item['cc']} | Курс:"
        f" {item['rate']}"
    )
else:
  print(f"Error: {response.status_code}")