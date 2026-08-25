import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    options = Options()

    options.add_argument("--start-maximized")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    yield driver

    driver.quit()
