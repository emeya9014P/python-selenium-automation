from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, end_url=''):
        self.driver.get(f'https://www.target.com/{end_url}')

    def get_current_url(self):
        return self.driver.current_url
    
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print("All windows before switching", all_windows)
        self.driver.switch_to.window(all_windows[1])
        print('Window after switch', self.get_current_window())

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print('Window after switch', self.get_current_window())

    def refresh_page(self):
        self.driver.refresh()

    def close_window(self):
        self.driver.close()

    def wait_until_clickable(self, *locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        )
        return element

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        ).click()

    def wait_until_appear(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element by {locator} not visible"
        )
        return element

    def wait_until_disappear(self, *locator):
        element = self.wait.until(
            EC.invisibility_of_element(locator),
            message=f"Element by {locator} still visible on the page"
        )
        return element

    def wait_until_url_contains(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f"Expected '{expected_partial_url}' not in '{self.driver.current_url}'"
        )

    def wait_until_url_to_be(self, expected_url): #find exact matched url
        self.wait.until(
            EC.url_to_be(expected_url),
            message=f"Expected '{expected_url}', but got '{self.driver.current_url}'"
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f"Expected '{expected_text}', but found '{actual_text}'"
        print(f"Test Passed: {expected_text}")

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text in actual_text, \
            f"Expected '{expected_partial_text}' not in '{actual_text}'"
        print(f"Test Passed: '{expected_partial_text}'")

