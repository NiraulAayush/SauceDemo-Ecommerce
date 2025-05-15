from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()