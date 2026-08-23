# Diploma_Kinopoisk
Автоматизация UI и API тестирования сайта Кинопоиск.

## Технологии

- Python
- Pytest
- Selenium WebDriver
- Requests
- Allure
- Page Object Model

## Структура проекта
api/
movie_api.py

pages/
main_page.py

tests/
test_api.py
test_ui.py
test_smoke.py

config/
config.py
## Запуск тестов

Установить зависимости:

```bash
pip install -r requirements.txt

Запуск всех тестов:

pytest -v

Запуск API:

pytest -m api

Запуск UI:

pytest -m ui

Создание Allure отчёта:

pytest --alluredir=allure-results

Просмотр:

allure serve allure-results

Для собеседования это будет выглядеть гораздо лучше.

---

# 8. Сейчас порядок действий

Делаем так:

### Шаг 1

Открываем `.gitignore`.

Добавляем в конец:

```gitignore
.idea/
allure-results/
allure-report/
Шаг 2

Проверяем:

git status
Шаг 3

Добавляем:

git add .
Шаг 4

Проверяем:

git status
Шаг 5

Коммит:

git commit -m "Add API and UI autotests for Kinopoisk"
Шаг 6

Отправляем:

git push origin main