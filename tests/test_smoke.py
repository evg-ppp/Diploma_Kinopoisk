import pytest
import allure

from api.movie_api import MovieAPI


@allure.feature("Smoke тестирование")
@allure.story("Проверка работоспособности API")
@allure.title("API доступно")
@pytest.mark.smoke
@pytest.mark.api
def test_api_smoke():

    api = MovieAPI()

    response = api.get_movie(301)

    assert response.status_code == 200
