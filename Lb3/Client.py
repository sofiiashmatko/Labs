import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:5000"
AUTH = HTTPBasicAuth("admin", "12345")


def get_items():
    print("\n=== GET ALL ITEMS ===")
    r = requests.get(BASE_URL + "/items", auth=AUTH)
    print("Status:", r.status_code)
    print("Response:", r.json())


def get_item(item_id):
    print(f"\n=== GET ITEM {item_id} ===")
    r = requests.get(BASE_URL + f"/items/{item_id}", auth=AUTH)
    print("Status:", r.status_code)
    print("Response:", r.json())


def add_item(item):
    print("\n=== ADD ITEM ===")
    r = requests.post(BASE_URL + "/items", json=item, auth=AUTH)
    print("Status:", r.status_code)
    print("Response:", r.json())


def update_item(item_id, data):
    print(f"\n=== UPDATE ITEM {item_id} ===")
    r = requests.put(BASE_URL + f"/items/{item_id}", json=data, auth=AUTH)
    print("Status:", r.status_code)
    print("Response:", r.json())


def delete_item(item_id):
    print(f"\n=== DELETE ITEM {item_id} ===")
    r = requests.delete(BASE_URL + f"/items/{item_id}", auth=AUTH)
    print("Status:", r.status_code)
    print("Response:", r.json())


# ==================================================
#                АВТОМАТИЧНЕ ТЕСТУВАННЯ
# ==================================================

if __name__ == "__main__":

    # 1. Зчитування всіх товарів
    get_items()

    # 2. Отримання товару за id
    get_item(3)

    # 3. Додавання НОВОГО товару
    add_item({
        "id": 10,
        "name": "Gaming Chair",
        "price": 199,
        "color": "black"
    })

    # 4. Перевірити, що товар додано
    get_items()

    # 5. Оновити товар
    update_item(10, {
        "price": 179,
        "color": "red"
    })

    # 6. Перевірити оновлення
    get_item(10)

    # 7. Видалити товар
    delete_item(10)

    # 8. Перевірити видалення
    get_items()

    print("\n=== TEST COMPLETED SUCCESSFULLY ===")
