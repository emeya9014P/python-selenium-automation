from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class SignInPage(BasePage):
    CONTINUE_BTN = (By.CSS_SELECTOR, "#login")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#username")
    ENTER_YOUR_PASSWORD_BTN = (By.CSS_SELECTOR, "#password")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_ERROR_MSG = (By.CSS_SELECTOR, "div[class*='styles_content']")
    SIGN_IN_WITH_PASSWORD_BTN = (By.XPATH, "//button[text()='Sign in with password']")
    TC_LINK = (By.CSS_SELECTOR, "a[aria-label='terms & conditions - opens in a new window']")
    TC_TITLE = (By.CSS_SELECTOR, "h1[data-test='page-title']")

    def open_sign_in_page(self):
        self.open_url(self.SIGNIN_PAGE_URL)
        self.wait_until_appear(*self.EMAIL_FIELD)
        # print(f"Connecting to: https://www.target.com/{self.SIGNIN_PAGE_URL}")

    def click_tp_link(self):
        self.wait_until_clickable_click(*self.TC_LINK)

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print("All windows before switching", all_windows)
        self.driver.switch_to.window(all_windows[1])
        print('Window after switch', self.get_current_window())

    def verify_terms_and_conditions_page_opened(self):
        element = self.wait_until_appear(*self.TC_TITLE)
        return element

    def close_window(self):
        self.driver.close()

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print('Window after switch', self.get_current_window())

    def enter_correct_email(self, email):
        element = self.wait_until_appear(*self.EMAIL_FIELD)
        element.clear()
        element.send_keys(email)

    def click_continue_btn(self):
        self.wait_until_clickable_click(*self.CONTINUE_BTN)

    def enter_your_password_btn(self):
        self.wait_until_clickable_click(*self.ENTER_YOUR_PASSWORD_BTN)

    def enter_incorrect_password(self, password):
        password = self.wait_until_appear(*self.PASSWORD_FIELD)
        actions = ActionChains(self.driver)
        actions.move_to_element(password).perform()
        # element = self.wait_until_appear(*self.PASSWORD_FIELD)
        # element.clear()
        # element.send_keys(password)

    def click_sign_in_with_password_btn(self):
        self.wait_until_clickable_click(*self.SIGN_IN_WITH_PASSWORD_BTN)

    def verify_error_message(self):
        self.wait_until_appear(*self.SIGN_IN_ERROR_MSG)


