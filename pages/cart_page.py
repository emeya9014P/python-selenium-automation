from pydoc import text

from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CartPage(Page):
    EMPTY_CART_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_cart_empty(self):
        actual_result = self.find_element(*self.EMPTY_CART_MSG).text
        expected_result = "Your cart is empty"
        assert expected_result == actual_result, f"Expected {expected_result}, but got {actual_result}"
        print("Test Passed")









