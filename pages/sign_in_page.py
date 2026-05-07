from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SignInPage(BasePage):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[#username]")
    SIGNIN_PAGE_URL = 'login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_request_username&signin_amr=true'
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

