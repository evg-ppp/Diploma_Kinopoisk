# Diploma_Kinopoisk

Автоматизация UI и API тестирования сайта Кинопоиск.

## Технологии

- Python 3.14
- Pytest
- Selenium WebDriver
- Requests
- Allure
- Page Object Model
- python-dotenv
- webdriver-manager

## Структура проекта

```
Diploma_Kinopoisk
│
├── api
│   └── movie_api.py
│
├── pages
│   └── main_page.py
│
├── tests
│   ├── test_api.py
│   ├── test_ui.py
│   └── test_smoke.py
│
├── config
│   └── config.py
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Запуск тестов

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск всех тестов:

```bash
pytest -v
```

Запуск API тестов:

```bash
pytest -m api
```

Запуск UI тестов:

```bash
pytest -m ui
```

Создание Allure отчёта:

```bash
pytest --alluredir=allure-results
```

Просмотр отчёта:

```bash
allure serve allure-results
```

## Проверка качества кода

Проверка PEP8 с помощью flake8:

```bash
flake8 api pages tests config conftest.py
```

## Покрытие тестами

### API

- Получение фильма по ID
- Поиск фильма по названию
- Проверка несуществующего фильма
- Проверка некорректных параметров

### UI

- Поиск фильма
- Открытие страницы фильма
- Переход по логотипу
- Открытие категории фильмов
- Открытие списка ТОП-250
