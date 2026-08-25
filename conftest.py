import os
import platform

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def allure_environment():
    environment = {
        "Python": platform.python_version(),
        "OS": platform.system(),
        "Browser": "Google Chrome",
        "Selenium": selenium.__version__,
        "Pytest": pytest.__version__,
    }

    os.makedirs("allure-results", exist_ok=True)

    with open(
        "allure-results/environment.properties",
        "w",
        encoding="utf-8",
    ) as file:
        for key, value in environment.items():
            file.write(f"{key}={value}\n")


@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--start-maximized")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)

    yield driver

    driver.quit()
