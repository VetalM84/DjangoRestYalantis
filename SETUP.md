Запускаем проект на своей машине: 

1. Клонируем репозиторий `git clone https://github.com/VetalM84/DjangoRestYalantis`
2. Переходим в папку с проектом `cd DjangoRestYalantis`
3. Устанавливаем виртуальное окружение `python -m venv env`
4. Запускаем виртуальное окружение `source env/Scripts/activate`
5. Обновляем pip `python -m pip install --upgrade pip`
6. Устанавливаем в виртуальном окружении зависимости для проекта `python -m pip install --no-cache-dir -r requirements.txt`
7. Делаем миграции для создания базы данных `python manage.py makemigrations && python manage.py migrate`
8. Заполняем данными модели `Driver` и `Vehicle` &mdash; `python manage.py loaddata db.json`
9. Запускаем локальный сервер `python manage.py runserver`
10. Маршруты доступны в файле README.md и test.http