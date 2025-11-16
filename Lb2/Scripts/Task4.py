from flask import Flask, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

def get_usd_rate(date_str):
    """Запит до API НБУ з датою у форматі YYYYMMDD"""
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date_str}&json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["rate"]
    return None


@app.route("/currency", methods=["GET"])
def currency():
    param = request.args.get(None)   # беремо перший параметр без значення

    today = datetime.now()
    yesterday = today - timedelta(days=1)

    if param == "today":
        date_str = today.strftime("%Y%m%d")
        rate = get_usd_rate(date_str)
        return f"USD today: {rate} грн"

    elif param == "yesterday":
        date_str = yesterday.strftime("%Y%m%d")
        rate = get_usd_rate(date_str)
        return f"USD yesterday: {rate} грн"

    else:
        return "Error: use ?today or ?yesterday"


if __name__ == '__main__':
    app.run(port=8000)
