from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as CS
from webdriver_manager.chrome import ChromeDriverManager

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://scruff.com")
    yield
    driver.quit()

