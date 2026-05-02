from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

STORY_CARDS_BLOCK = (By.CSS_SELECTOR, "div[data-test='@web/SlingshotComponents/Storyblocks'] a")

@given("Open Target Circle page")
def open_target_circle_page(context):
    context.app.target_circle_page.open_target_circle_page()


@then ("Verify 2 story_cards are shown")
def verify_story_cards_count(context):
    context.app.target_circle_page.verify_story_cards_count()


# header links: elements (always return something like [])
# @then("Verify 6 links are shown")
# def verify_header_link_amount(context):
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")
#     print('header links: ')
#     print(links)
#     assert len(links) == 6, f'Expected 6 links, but got {len(links)}'