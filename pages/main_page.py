from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.NAME, "text")
            )
        )

    def find_search_input(self):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.NAME, "text")
            )
        )

    def open_movie(self, movie_id: int) -> None:
        self.driver.get(
            f"{BASE_URL}/film/{movie_id}/"
        )

        WebDriverWait(self.driver, 20).until(
            EC.url_contains(
                f"/film/{movie_id}/"
            )
        )

    def click_logo(self) -> None:
        logo = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'a[aria-label="Кинопоиск"]'
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logo
        )

        WebDriverWait(self.driver, 20).until(
            EC.url_to_be(
                "https://www.kinopoisk.ru/"
            )
        )

    def open_menu(self) -> None:
        menu_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Меню"]')
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            menu_button
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver:
            driver.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Меню"]'
            ).get_attribute("aria-expanded") == "true"
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(@href,'/lists/categories/movies/1/')]"
                )
            )
        )

    def open_movies(self) -> None:
        self.driver.get(
            f"{BASE_URL}/lists/categories/movies/1/"
        )

        WebDriverWait(self.driver, 20).until(
            EC.url_contains(
                "/lists/categories/movies/1/"
            )
        )

    def open_top_250(self) -> None:
        self.driver.get(
            f"{BASE_URL}/lists/movies/top250/"
        )

        WebDriverWait(self.driver, 20).until(
            EC.url_contains(
                "/lists/movies/top250/"
            )
        )


