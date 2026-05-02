from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    ACCOUNT_BTN = (By.CSS_SELECTOR, "#account-sign-in")
    SIGN_IN_BTN_SIDE_NAV = (By.XPATH, "//button[contains(text(),'Sign in')]")
    HEADER_LINKS_CONTAINER = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")
    HEADER_LINKS = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")

    def search_product(self, search_query: str):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_cart(self):
        self.click(*self.CART_ICON)
        sleep(2)

    def click_account_btn(self):
        self.click(*self.ACCOUNT_BTN)
        sleep(2)

    def verify_signin_button_opened(self):
        element = self.find_element(*self.SIGN_IN_BTN_SIDE_NAV)
        sleep(2)

        actual_result = element.text
        expected_result = "Sign in or create account"

        assert expected_result in actual_result, f"Expected {expected_result}, but got {actual_result}"
        print("Test passed")

    def verify_header_links_container_shown(self):
        element = self.find_element(*self.HEADER_LINKS_CONTAINER)
        sleep(2)

        assert element.is_displayed() is True, f"Header links container is not shown"
        print("Test passed")

    def verify_header_links_count(self):
        links = self.find_elements(*self.HEADER_LINKS)
        sleep(2)

        assert len(links) == 6, f"Expected 6, but got {len(links)}"
        print(f"{len(links)} links are shown")