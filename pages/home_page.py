import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class HomePage(BasePage):
      def __init__(self):            
            self.driver = conftest.driver
            self.link_advertise = (By.XPATH, "//h4[@class='nav desktop' and text()='advertise']")
            self.title_browse = (By.XPATH, "//h2[@id='browse']") 
           



      def nav_to_advertise(self):
            self.finder(self.link_advertise).click()
            
            

      

     

