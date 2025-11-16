import requests
from datetime import datetime, timedelta

# Код валюти
VALCODE = "HUF"

# Поточна дата
today = datetime.now()

# Отримуємо курси за останні 7 днів
print(f"Курс {VALCODE} за останній тиждень:\n")

for i in range(1, 8):
    date = today - timedelta(days=i)
    date_str = date.strftime("%Y%m%d")  # формат YYYYMMDD для API НБУ
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={VALCODE}&date={date_str}&json"

    response = requests.get(url)
    data = response.json()

    if data:
        rate = data[0]["rate"]
        exchangedate = data[0]["exchangedate"]
        print(f"{exchangedate}: {rate:.4f} грн")
    else:
        print(f"{date.strftime('%d.%m.%Y')}: дані відсутні")
