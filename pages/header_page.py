from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Header(Page):
    ACCOUNT_BTN = (By.CSS_SELECTOR, "#account-sign-in")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    HEADER_LINKS_CONTAINER = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")
    HEADER_LINKS = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_RESULT_TEXT = (By.CSS_SELECTOR, "div[data-test='text-quill']")
    SIDE_NAV_CONTAINER = (By.CSS_SELECTOR, "[data-test='content-wrapper']")
    SIGN_IN_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test = 'accountNav-signIn']")
    SIGN_IN_HEADER = (By.XPATH, "//h1[text()='Sign in or create account']")

    def search_product(self, search_query: str):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.wait_until_clickable_click(*self.SEARCH_BTN)
        self.wait_until_appear(*self.SEARCH_RESULT_TEXT)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_account_btn(self):
        self.wait_until_clickable_click(*self.ACCOUNT_BTN)

    def click_sign_in_navigation_menu(self):
        self.wait_until_appear(*self.SIDE_NAV_CONTAINER)
        self.wait_until_clickable_click(*self.SIGN_IN_BTN_SIDE_NAV)

    def verify_signin_form_opened(self):
        element = self.wait_until_appear(*self.SIGN_IN_HEADER)

        actual_result = element.text
        expected_result = "Sign in or create account"

        assert expected_result in actual_result, f"Expected {expected_result}, but got {actual_result}"
        print("Test passed: '{Sign in or create account}' is appeared.")


    def verify_header_links_container_shown(self):
        element = self.wait_until_appear(*self.HEADER_LINKS_CONTAINER)

        assert element.is_displayed() is True, f"Header links container is not shown"
        print("Test passed")

    def verify_header_links_count(self):
        links = self.wait_until_appear(*self.HEADER_LINKS)

        assert len(links) == 6, f"Expected 6, but got {len(links)}"
        print(f"{len(links)} links are shown")

