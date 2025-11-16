from flask import Flask, request

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def currency():
    # Отримуємо параметри з URL
    today = request.args.get("today")
    key = request.args.get("key")

    # Статичний курс валюти GBP
    gbp_rate = "GBP - 48.2"


    return f"Currency rate today: {gbp_rate}. Request params: today={today}, key={key}"

if __name__ == '__main__':
    app.run(port=8000)
