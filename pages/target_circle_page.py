from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class TargetCirclePage(Page):
    STORY_CARDS_BLOCK = (By.CSS_SELECTOR, "div[data-test='@web/SlingshotComponents/Storyblocks'] a")

    def open_target_circle_page(self):
        self.open_url('circle')

    def verify_story_cards_count(self):
        story_cards = self.driver.find_elements(*self.STORY_CARDS_BLOCK)

        print('story_cards found: ')
        print(len(story_cards))
        assert len(story_cards) == 2, f"Expected 2 story_cards, but found {len(story_cards)}"
