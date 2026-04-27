from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target Circle page")
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    sleep(3)


@then ("Verify 2 storycards are shown")
def verify_storycards_count(context):
    storycards = context.driver.find_elements(By.CSS_SELECTOR, "div[data-test='@web/SlingshotComponents/Storyblocks'] a")
    print('storycards found: ')
    print(len(storycards))
    assert len(storycards) == 2, f"Expected 2 storycards, but found {len(storycards)}"


# header links: elements (always return something like [])
# @then("Verify 6 links are shown")
# def verify_header_link_amount(context):
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")
#     print('header links: ')
#     print(links)
#     assert len(links) == 6, f'Expected 6 links, but got {len(links)}'