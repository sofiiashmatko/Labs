import requests
from datetime import datetime, timedelta


def build_nbu_url(valcode: str, date_str: str) -> str:
    """Формує URL для API НБУ"""
    return (
        "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
        f"?valcode={valcode}&date={date_str}&json"
    )


def get_rate_for_date(valcode: str, date: datetime) -> tuple[str, float] | None:
    """Отримує курс валюти за конкретну дату"""
    date_str = date.strftime("%Y%m%d")
    url = build_nbu_url(valcode, date_str)

    response = requests.get(url)
    data = response.json()

    if not data:
        return None

    return data[0]["exchangedate"], data[0]["rate"]


def get_week_rates(valcode: str, today: datetime | None = None) -> list[tuple[str, float]]:
    """Отримує курси валюти за попередні 7 днів"""
    today = today or datetime.now()
    results = []

    for i in range(1, 8):
        day = today - timedelta(days=i)
        rate = get_rate_for_date(valcode, day)
        if rate:
            results.append(rate)

    return results
