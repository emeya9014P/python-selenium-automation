from pydoc import text

from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CartPage(Page):
    EMPTY_CART_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_cart_empty(self):
        self.wait.until(*self.EMPTY_CART_MSG)
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MSG)









