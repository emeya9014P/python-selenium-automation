from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target Help page")
def open_target_help_page(context):
    context.driver.get("https://help.target.com/help")
    sleep(2)


# @then("Verify Help text is shown")
# def verify_help_is_shown(context):
#     context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Help')]")
#     actual_result = "Help"
#     assert "Help" in actual_result, f'Expected Help, but got {actual_result}'
#     print("Test passed")


@then("Verify {expected_text} text is shown")
def verify_text_is_shown(context, expected_text):
    sleep(3)
    element = context.driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(expected_text))
    actual_result = element.get_attribute('innerText')
    assert expected_text in actual_result, f'Expected {expected_text}, but got {actual_result}'
    print("Test passed")

# header links: elements (여러 개를 한꺼번에 처리할 때는 무조건 복수형! always return something like [])
@then("Verify 9 cards are linked")
def verify_cards_link_amount(context):
    sleep(3)
    links = context.driver.find_elements(By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper'] a")
    actual_result = len(links)
    assert len(links) == 9, f'Expected 9 links, but got {len(links)}'
    print(links)

@then("Verify 8 horizontal cards are linked")
def verify_cards_link_amount(context):
    sleep(3)
    all_cards = context.driver.find_elements(By.CSS_SELECTOR, "div[class*='LinkItem_linkList'][data-test='LinkList']")
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_cards[0])
    sleep(3)

    actual_result = len(all_cards)
    assert actual_result == 8, f'Expected 8 links, but got {actual_result}'
    print(len(all_cards))