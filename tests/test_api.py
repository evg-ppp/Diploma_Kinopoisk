import pytest
import allure

from api.movie_api import MovieAPI


@allure.feature("API тестирование")
@allure.story("Получение фильма")
@allure.title("Получение фильма по ID")
@pytest.mark.api
def test_get_movie():
    api = MovieAPI()

    response = api.get_movie(301)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 301


@allure.feature("API тестирование")
@allure.story("Поиск фильма")
@allure.title("Поиск фильма по названию")
@pytest.mark.api
def test_search_movie():
    api = MovieAPI()

    response = api.search_movie("Матрица")

    assert response.status_code == 200

    data = response.json()

    assert data["docs"][0]["name"] == "Матрица"


@allure.feature("API тестирование")
@allure.story("Получение фильма")
@allure.title("Получение фильма с некорректным ID")
@pytest.mark.api
def test_get_movie_invalid_id():
    api = MovieAPI()

    response = api.get_movie(999999999)

    assert response.status_code == 400

    data = response.json()

    assert data["statusCode"] == 400
    assert data["error"] == "Bad Request"
    assert data["message"][0] == (
        "Значение поля id должно быть в диапазоне от 250 до 15000000!"
    )


@allure.feature("API тестирование")
@allure.story("Поиск фильма")
@allure.title("Поиск фильма, которого нет")
@pytest.mark.api
def test_search_movie_not_found():
    api = MovieAPI()

    response = api.search_movie("ФильмКоторогоТочноНет123456")

    assert response.status_code == 200

    data = response.json()

    assert data["docs"] == []
    assert data["total"] == 0


@allure.feature("API тестирование")
@allure.story("Поиск фильма")
@allure.title("Поиск фильма с некорректным номером страницы")
@pytest.mark.api
def test_search_movie_invalid_page():
    api = MovieAPI()

    response = api.search_movie(
        "string",
        page=0,
        limit=10
    )

    assert response.status_code == 400

    data = response.json()

    assert data["statusCode"] == 400
    assert data["error"] == "Bad Request"
    assert "page must not be less than 1" in data["message"][0]
