from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


HORIZONTAL_CARD = (By.CSS_SELECTOR, "div[class*='LinkItem_linkList'][data-test='LinkList']")
NAV_CARD = (By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper'] a")


@given("Open Target Help page")
def open_target_help_page(context):
    context.app.target_help_page.open_target_help_page()


@then("Verify {expected_text} text is shown")
def verify_text_is_shown(context, expected_text):
    context.app.target_help_page.verify_text_displayed(expected_text)


# header links: elements (여러 개를 한꺼번에 처리할 때는 무조건 복수형! always return something like [])
@then("Verify 9 cards are linked")
def verify_9_cards_link_amount(context):
    context.app.target_help_page.verify_9_cards_linked()


@then("Verify 8 horizontal cards are linked")
def verify_8_cards_link_amount(context):
    context.app.target_help_page.verify_8_horizontal_cards_linked()
