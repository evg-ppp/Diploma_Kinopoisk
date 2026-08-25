# Diploma_Kinopoisk

Автоматизация UI и API тестирования сайта Кинопоиск.

Проект создан в рамках дипломной работы по автоматизации тестирования.  
Реализованы UI-тесты с использованием Selenium WebDriver и API-тесты с использованием Requests.

---

## Технологии

- Python 3.14
- Pytest
- Selenium WebDriver
- Requests
- Allure Report
- Page Object Model
- pytest markers
- python-dotenv
- webdriver-manager
- flake8

---

## Структура проекта

```text
Diploma_Kinopoisk
│
├── api
│   └── movie_api.py          # API методы работы с фильмами
│
├── pages
│   └── main_page.py          # Page Object для UI тестов
│
├── tests
│   ├── test_api.py           # API тесты
│   ├── test_ui.py            # UI тесты
│   └── test_smoke.py         # Smoke тесты
│
├── config
│   └── config.py             # Настройки проекта
│
├── conftest.py               # Pytest фикстуры
├── pytest.ini                # Настройки pytest
├── requirements.txt          # Зависимости проекта
└── README.md
```

---

## Установка проекта

Клонировать репозиторий:

```bash
git clone https://github.com/evg-ppp/Diploma_Kinopoisk.git
```

Перейти в папку проекта:

```bash
cd Diploma_Kinopoisk
```

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать виртуальное окружение:

Windows:

```bash
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

---

## Настройка окружения

Создать файл `.env` в корне проекта:

```env
API_KEY=your_api_key
```

API ключ используется для работы с Kinopoisk API.

---

## Запуск тестов

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

Запуск Smoke тестов:

```bash
pytest -m smoke
```

---

## Allure Report

Создание Allure отчёта:

```bash
pytest --alluredir=allure-results
```

Просмотр отчёта:

```bash
allure serve allure-results
```

В отчёте отображаются:

- результаты выполнения тестов;
- группы API/UI/Smoke тестов;
- время выполнения;
- окружение запуска.

---

## Проверка качества кода

Проверка PEP8 с помощью flake8:

```bash
flake8 api pages tests config conftest.py
```

---

## Покрытие тестами

### API

Проверяется:

- получение фильма по ID;
- поиск фильма по названию;
- проверка несуществующего фильма;
- проверка некорректных параметров запроса.

### UI

Проверяется:

- поиск фильма;
- открытие страницы фильма;
- переход на главную страницу по логотипу;
- открытие категории фильмов;
- открытие списка ТОП-250.

### Smoke

Проверяется:

- доступность API.

---

## Результат выполнения

Текущий результат:

```
11 passed
```

Все UI и API тесты проходят успешно.
