from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(3)


@when("Click Account button")
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
    sleep(3)


@then("Verify sign in button opened")
def verify_signin_button_open(context):
    actual_result = context.driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").text
    expected_result = "Sign in or create account"
    assert "Sign in or create account" in actual_result
    print("Test passed")


@when("Search for {product}")
def search_for_tea(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(3)

# @when("Search for tea")
# def search_for_tea(context):
#     context.driver.find_element(*SEARCH_FIELD).send_keys("tea")
#     context.driver.find_element(*SEARCH_BTN).click()
#     sleep(3)

# header link: element
@then("Verify header link container is shown")
def verify_header_links(context):
    e = context.driver.find_element(By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")
    print('header link container: ')
    print(e)

# header links: elements (여러 개를 한꺼번에 처리할 때는 무조건 복수형! always return something like [])
@then("Verify 6 links are shown")
def verify_header_link_amount(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")
    print('header links: ')
    print(links)
    assert len(links) == 6, f'Expected 6 links, but got {len(links)}'