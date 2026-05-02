from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class TargetHelpPage(Page):
    NAV_CARD = (By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper'] a")
    HORIZONTAL_CARD = (By.CSS_SELECTOR, "div[class*='LinkItem_linkList'][data-test='LinkList']")


    def open_target_help_page(self):
        self.open_url('help')

    def verify_text_displayed(self, expected_text):
        TEXT_LOCATOR = (By.XPATH, f"//*[contains(text(), '{expected_text}')]")

        element = self.find_element(*TEXT_LOCATOR)

        actual_result = element.get_attribute('innerText')
        assert expected_text in actual_result, f'Expected {expected_text}, but got {actual_result}'
        print(f"Test passed: verified Target text '{expected_text}' is displayed. (Actual: {actual_result})")

    def verify_9_cards_linked(self):
        cards = self.find_elements(*self.NAV_CARD)

        actual_result = len(cards)
        assert len(cards) == 9, f'Expected 9 cards are linked, but got {len(cards)}'
        print(f"Test Passed: verified {actual_result} cards are linked")

    def verify_8_horizontal_cards_linked(self):
        horizontal_cards = self.find_elements(*self.HORIZONTAL_CARD)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", horizontal_cards[0])

        actual_result = len(horizontal_cards)
        assert actual_result == 8, f'Expected 8 cards, but got {actual_result}'
        print(f"Test passed: verified {actual_result} cards are linked")