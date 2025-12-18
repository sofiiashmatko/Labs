import pytest
from datetime import datetime
from unittest.mock import patch

from nbu_week_rate import (
    build_nbu_url,
    get_rate_for_date,
    get_week_rates,
)


# ---------- build_nbu_url (2 тести) ----------
def test_build_nbu_url_contains_valcode_and_date():
    url = build_nbu_url("HUF", "20250101")
    assert "valcode=HUF" in url
    assert "date=20250101" in url


def test_build_nbu_url_starts_with_nbu_domain():
    url = build_nbu_url("USD", "20240101")
    assert url.startswith("https://bank.gov.ua")


# ---------- get_rate_for_date (2 тести) ----------
@patch("nbu_week_rate.requests.get")
def test_get_rate_for_date_success(mock_get):
    mock_get.return_value.json.return_value = [
        {"rate": 10.1234, "exchangedate": "01.01.2025"}
    ]

    result = get_rate_for_date("HUF", datetime(2025, 1, 1))
    assert result == ("01.01.2025", 10.1234)


@patch("nbu_week_rate.requests.get")
def test_get_rate_for_date_no_data(mock_get):
    mock_get.return_value.json.return_value = []

    result = get_rate_for_date("HUF", datetime(2025, 1, 1))
    assert result is None


# ---------- get_week_rates (2 тести) ----------
@patch("nbu_week_rate.get_rate_for_date")
def test_get_week_rates_returns_list(mock_get_rate):
    mock_get_rate.return_value = ("01.01.2025", 10.0)

    result = get_week_rates("HUF", today=datetime(2025, 1, 8))
    assert len(result) == 7


@patch("nbu_week_rate.get_rate_for_date")
def test_get_week_rates_skips_none(mock_get_rate):
    mock_get_rate.side_effect = [
        None,
        ("02.01.2025", 10.0),
        None,
        ("04.01.2025", 11.0),
        None,
        ("06.01.2025", 12.0),
        None,
    ]

    result = get_week_rates("HUF", today=datetime(2025, 1, 8))
    assert len(result) == 3
