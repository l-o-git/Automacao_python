import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.webdriver.support.select import Select


class AdvertisePage(BasePage):
      def __init__(self):            
            self.driver = conftest.driver
            self.link_perry = (By.XPATH,"//a[@class='logo-link w-nav-brand']")
            self.input_organization = (By.XPATH, "//input[@aria-label='name']")
            self.input_full_name = (By.XPATH, "//input[@aria-label='text7']")
            self.br_flag = (By.XPATH, "//img[@alt='Brazil flag']")
            self.dropdown = (By.XPATH, "//input[@aria-label='Dropdown input']")
            self.input_phone = (By.XPATH, "//input[@aria-label='Número de telefone sem o código do país']")
            self.input_email = (By.XPATH, "//input[@aria-labelledby='email']")
            self.input_website = (By.XPATH, "//input[@aria-labelledby='link']")
            self.input_message = (By.XPATH, "//input[@aria-label='text3']")
            self.button_send = (By.XPATH,"//button[@data-testid='button' and text()='Enviar']")
            self.iFrameA = (By.XPATH, "//iframe[@style='border: 0; box-shadow: 5px 5px 56px 0px rgba(0,0,0,0.25);']")
            self.iFrameB = (By.XPATH, "//iframe[@style='position: absolute; top: 0px; left: 0px; border: none; visibility: hidden;']")
            self.dropHear = (By.XPATH, "(//*[@class='dropdown-indicator css-1au5vl6-indicatorContainer'])[2]")   
            self.inputHear = (By.XPATH, "//input[@id='react-select-3-input']")
     
      
      def fill_media_form(self):
            assert  self.finder(self.link_perry).is_displayed       
            self.driver.switch_to.frame(self.finder(self.iFrameA))
            self.finder(self.input_organization).send_keys("Hélio's Company")
            self.finder(self.input_full_name).send_keys("Hélio Castro")
            self.finder(self.dropdown).click()
            self.finder(self.dropdown).send_keys("55")
            self.finder(self.dropdown).send_keys("\n")
            self.finder(self.input_phone).send_keys("11970459624")
            self.finder(self.input_email).send_keys("helio.castrosp@outlook.com")
            self.finder(self.input_website).send_keys("https://linkedin.com/castrohelio")
            self.finder(self.input_message).send_keys("Hey there!")
            self.finder(self.dropHear).click()          
            self.finder(self.inputHear).send_keys("C")
            self.finder(self.inputHear).send_keys("\n")
            self.finder(self.inputHear).send_keys("\n")
         

      def assert_send(self):
            assert self.finder(self.button_send).is_enabled
            #didn't submit to not register the data on your prd db





            

      

     

