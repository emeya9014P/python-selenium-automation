from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from time import sleep

class TargetHelpPage(BasePage):
    HORIZONTAL_CARD = (By.CSS_SELECTOR, "div[class*='LinkItem_linkList'][data-test='LinkList']")
    NAV_CARD = (By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper'] a")
    ORDERS_PURCHASES_HEADER = (By.XPATH, "//h1[contains(text(), ' Print a receipt')]")
    RETURNS_HEADER = (By.XPATH, "//h1[text()='Returns']")
    PROMOTIONS_HEADER = (By.XPATH, "//h1[text()=' Current promotions']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_HELP_FIELD = (By.CSS_SELECTOR, "input[title='search help']")
    SELECT_TOPIC_DD = (By. CSS_SELECTOR, "select[id*= 'viewHelpTopics']")
    TARGET_CIRCLE_HEADER = (By.XPATH, "//h1[contains(text(), 'About Target Circle')]")

    # Dynamic locator for Verification e.g., "Verify help Current promotions page opened" => modify locator od the elements during the test execution
    HEADER = (By.XPATH, "//h1[contains(text(), '{SUBSTR}')]")

    def get_header_locator(self, expected_text):
        # return [By.XPATH ,    "//h1[text()=' expected_text']
        # return (By.XPATH, f"//h1[contains(text(), '{expected_text}')]")
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTR}', expected_text)]

    def verify_header_present(self, expected_text):
        locator = self.get_header_locator(expected_text)
        self.wait_until_appear(*locator)

    def open_target_help_page(self):
        self.open_url('help')
        self.wait_until_appear(*self.SEARCH_FIELD)

    def verify_text_displayed(self, expected_text):
        TEXT_LOCATOR = (By.XPATH, f"//*[contains(text(), '{expected_text}')]")

        element = self.wait_until_appear(*TEXT_LOCATOR)

        actual_result = element.get_attribute('innerText')
        assert expected_text in actual_result, f'Expected {expected_text}, but got {actual_result}'
        print(f"Test passed: verified Target text '{expected_text}' is displayed. (Actual: {actual_result})")

    def verify_9_cards_linked(self):
        self.wait_until_appear(*self.NAV_CARD)

        cards = self.find_elements(*self.NAV_CARD)

        actual_result = len(cards)
        assert len(cards) == 9, f'Expected 9 cards are linked, but got {len(cards)}'
        print(f"Test Passed: verified {actual_result} cards are linked")

    def verify_8_horizontal_cards_linked(self):
        self.wait_until_appear(*self.HORIZONTAL_CARD)

        horizontal_cards = self.find_elements(*self.HORIZONTAL_CARD)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", horizontal_cards[0])

        actual_result = len(horizontal_cards)
        assert actual_result == 8, f'Expected 8 cards, but got {actual_result}'
        print(f"Test passed: verified {actual_result} cards are linked")

    def open_target_help_returns_page(self):
        self.driver.get("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")
        self.wait_until_appear(*self.SEARCH_HELP_FIELD)

    def select_topic(self, returns_topic):
        dropdown = self.find_element(*self.SELECT_TOPIC_DD)
        select = Select(dropdown)
        select.select_by_value(returns_topic)

    # def verify_current_promotions_page_opened(self):
    #     self.wait_until_appear(*self. PROMOTIONS_HEADER)
    #
    # def verify_about_target_circle_page_opened(self):
    #     self.wait_until_appear(*self. TARGET_CIRCLE_HEADER)
