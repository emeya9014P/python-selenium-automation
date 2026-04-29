from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("Open Target Help page")
def open_target_help_page(context):
    context.driver.get("https://help.target.com/help")
    context.wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Help']")),
        message="Target Help page not found"
    )


@then("Verify {expected_text} text is shown")
def verify_text_is_shown(context, expected_text):
    element = context.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '{}')]".format(expected_text))),
              message="Verify text is not shown"
    )
    actual_result = element.get_attribute('innerText')
    assert expected_text in actual_result, f'Expected {expected_text}, but got {actual_result}'
    print("Test passed")


# header links: elements (여러 개를 한꺼번에 처리할 때는 무조건 복수형! always return something like [])
@then("Verify 9 cards are linked")
def verify_9_cards_link_amount(context):
    links = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper'] a")),
        message="9 cards are not linked"
    )
    actual_result = len(links)
    assert len(links) == 9, f'Expected 9 cards are linked, but got {len(links)}'
    print("Test Passed")


@then("Verify 8 horizontal cards are linked")
def verify_8_cards_link_amount(context):
    all_cards = context.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class*='LinkItem_linkList'][data-test='LinkList']")),
        message="8 horizontal cards are not linked"
    )
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_cards[0])

    actual_result = len(all_cards)
    assert actual_result == 8, f'Expected 8 links, but got {actual_result}'
    print(len(all_cards))