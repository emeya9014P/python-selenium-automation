from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')

    def open_main(self):
        self.open_url()
        self.wait_until_appear(*self.SEARCH_FIELD)