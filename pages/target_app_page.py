from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class TargetAppPage(BasePage):
    PP_LINK = (By.CSS_SELECTOR, "a[aria-label*='privacy policy']")

    def open_target_app_page(self):
        self.open_url('c/target-app/-/N-4th2r')
        self.wait_until_url_contains('c/target-app')

    def click_pp_link(self):
        self.wait_until_clickable_click(*self.PP_LINK)

