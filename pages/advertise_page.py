import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.webdriver.support.select import Select


class AdvertisePage(BasePage):
      def __init__(self):            
            self.driver = conftest.driver
            self.link_perry = (By.XPATH,"//a[@class='logo-link w-nav-brand']")
            self.input_organization = (By.XPATH, "//input[@aria-labelledby='name']")
            self.input_full_name = (By.XPATH, "//input[@aria-labelledby='text7']")
            self.br_flag = (By.XPATH, "//img[@alt='Brazil flag']")
            self.dropdown = (By.XPATH, "//input[@aria-label='Dropdown input']")
            self.input_phone = (By.XPATH, "//input[@aria-label='Número de telefone sem o código do país']")
            self.input_email = (By.XPATH, "//input[@aria-labelledby='email']")
            self.input_website = (By.XPATH, "//input[@aria-labelledby='link']")
            self.input_message = (By.XPATH, "//input[@aria-labelledby='text3']")
            self.button_send = (By.XPATH,"//button[@data-testid='button' and text()='Enviar']")
            self.iFrame = (By.XPATH, "//iframe")
               
     
      
      def fill_media_form(self):
            assert  self.finder(self.link_perry).is_displayed          
            self.driver.switch_to.frame(self.finder(self.iFrame))
            self.finder(self.input_organization).send_keys("Hopefully Perry Street Software")
            self.finder(self.input_full_name).send_keys("Hélio Castro")
            self.finder(self.dropdown).click()
            self.finder(self.dropdown).send_keys("55")
            self.finder(self.br_flag).click()
            self.finder(self.input_phone).send_keys("11970459624")
            self.finder(self.input_email).send_keys("helio.castrosp@outlook.com")
            self.finder(self.input_website).send_keys("https://linkedin.com/castrohelio")
            self.finder(self.input_message).send_keys("Hey there! hire me lol haha")
            time.sleep(3)

            

      def assert_send(self):
            assert self.finder(self.button_send).is_enabled





            

      

     

