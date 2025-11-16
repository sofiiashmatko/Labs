from flask import Flask, request

app = Flask(__name__)

@app.route("/save", methods=["POST"])
def save_text():
    # Отримуємо текстові дані з тіла запиту
    text_data = request.data.decode("utf-8")

    # Шлях до файла
    file_path = "saved_text.txt"

    # Записуємо у файл (режим append — додає новий текст)
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text_data + "\n")

    return f"Data saved successfully! Saved text: {text_data}"

if __name__ == '__main__':
    app.run(port=8000)
