import conftest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self):
            self.driver = conftest.driver
    
    def finder(self, locator):
        return self.driver.find_element(*locator)

    def wait_until(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    
