# Звіт з лабораторної роботи №2 студентки гр. КУІБ-22-1 Шматко Софії

# Завдання
1. [Easy] Встановити python веб фреймворк та запустити веб сервер на порту 8000.

Результат виконання:
   
![Скріншот результату виконання запиту](Pictures/Task1.png)

![Скріншот результату виконання запиту](Pictures/Task1_result.png)

Програмний код для виконання завдання: **[Task1.py](Scripts/task1.py)**

2. [Easy] Написати просту обробку запиту метода GET сервером. На запит повертати строку “Hello World!” 
Програмний код для виконання завдання: **[Task2.py](Scripts/task2.py)**

  ![Скріншот результату](Pictures/Task2.png)

  ![Скріншот результату](Pictures/Task2_1.png)
  
3.	[Easy-Medium] Написати просту обробку запиту метода GET сервером зі шляхом та параметрами в URL, наприклад http://127.0.0.1:8000/currency?today&key=value. Повертати статичне значення курса валют, наприклад “USD - 41,5”.  Для flask отримати параметри запиту за допомогою request.args.get(), для bottle -  request.query()   

Програмний код для виконання завдання: **[Task3.py](Scripts/Task3.py)**

![Скріншот результату](Pictures/Task3.png)

4.	[Medium] Обробка заголовків запиту. В залежності від значення параметру заголовку “Content-Type” (application/json чи application/xml) повертати json чи xml документ. У разі відсутності - повертати звичайний текст. Для flask отримати заголовки за допомогою request.headers.get, для bottle - request.get_header[]. 

Програмний код для виконання завдання: **[Task4.py](Scripts/Task4.py)**
 - xml
   
![Скріншот результату](Pictures/Task4_json_xml.png)

- plain text
  
  ![Скріншот результату](Pictures/Task4_plaintext.png)

5.	[Medium-Hard]  Написати обробку запиту метода GET сервером зі шляхом та параметрами в URL http://127.0.0.1:800/currency?<param>, де допустимі значення param:
a.	today - курс USD, актуальний на сьогодні

![Скріншот результату](Pictures/Task5_today.png)

b.	yesterday -  курс USD, актуальний на попередній день

![Скріншот результату](Pictures/Task5_yesterday.png)

Курси валют запитувати динамічно у програмі з офіційного сайту НБУ, згідно API специфікації - https://bank.gov.ua/admin_uploads/article/Instr_API_KURS_VAL_data.pdf

Програмний код для виконання завдання: **[Task5.py](Scripts/Task5.py)**

6.	[Hard] Написати обробку методу POST веб-сервером. У тілі повідомлення передавати текстові дані. Зберегти ці дані на сервері:
a.	[Easy] у файл

![Скріншот результату](Pictures/Task6.png)

Програмний код для виконання завдання: **[Task6.py](Scripts/Task6.py)**


![Скріншот результату](Pictures/Task5_chatbot_commands.png)


