from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    SEARCH_FIELD = (By.ID, 'search')

    def open_main(self):
        self.driver.get('https://www.target.com/')
        self.handle_health_consent()
        self.wait_until_appear(*self.SEARCH_FIELD)