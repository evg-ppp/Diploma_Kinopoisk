import allure
import pytest

from pages.main_page import MainPage


@allure.feature("UI тестирование")
@allure.story("Поиск фильма")
@allure.title("Поиск фильма по названию")
@pytest.mark.ui
def test_search_movie(driver):

    page = MainPage(driver)

    page.open()

    search = page.find_search_input()

    search.send_keys("Матрица")

    assert search.get_attribute("value") == "Матрица"


@allure.feature("UI тестирование")
@allure.story("Открытие фильма")
@allure.title("Открытие страницы фильма Матрица")
@pytest.mark.ui
def test_open_movie(driver):
    page = MainPage(driver)

    page.open_movie(301)

    assert "/film/301/" in driver.current_url

    assert "Матрица" in driver.title


@allure.feature("UI тестирование")
@allure.story("Навигация")
@allure.title("Переход на главную страницу по логотипу")
@pytest.mark.ui
def test_click_logo(driver):

    page = MainPage(driver)

    page.open()

    page.click_logo()

    assert driver.current_url == "https://www.kinopoisk.ru/"


@allure.feature("UI тестирование")
@allure.story("Списки фильмов")
@allure.title("Открытие категории фильмов")
@pytest.mark.ui
def test_open_movies(driver):

    page = MainPage(driver)

    page.open_movies()

    assert "/lists/categories/movies/1/" in driver.current_url


@allure.feature("UI тестирование")
@allure.story("Списки фильмов")
@allure.title("Открытие списка 250 лучших фильмов")
@pytest.mark.ui
def test_open_top_250(driver):

    page = MainPage(driver)

    page.open_top_250()

    assert "/lists/movies/top250/" in driver.current_url
