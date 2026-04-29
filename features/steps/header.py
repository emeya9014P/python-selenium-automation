from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@when("Click on Cart icon")
def click_cart_icon(context):
    context.wait.until(
        EC.element_to_be_clickable(CART_ICON),
        message="Cart icon not clickable"
    ).click()


@when("Click Account button")
def click_account(context):
    context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#account-sign-in")),
        message="Account button not clickable"
    ).click()


@then("Verify sign in button opened")
def verify_signin_button_open(context):
    element = context.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Sign in')]")),
        message="Sign in button not opened"
    )
    actual_result = element.text
    expected_result = "Sign in or create account"
    assert expected_result in actual_result, f"Expected {expected_result}, but got {actual_result}"
    print("Test passed")


@when("Search for {product}")
def search_for_coffee(context, product):
    element = context.wait.until(
        EC.visibility_of_element_located((SEARCH_FIELD)),
        message="Search for {product} not visible"
    )
    element.send_keys(product)

    context.wait.until(
        EC.visibility_of_element_located((SEARCH_BTN)),
        message="Search button not visible"
    ).click()


# @when("Search for tea")
# def search_for_tea(context):
#     context.driver.find_element(*SEARCH_FIELD).send_keys("tea")
#     context.driver.find_element(*SEARCH_BTN).click()
#     sleep(3)

# header link: element
@then("Verify header link container is shown")
def verify_header_links(context):
    e = context.wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")),
        message="Header link container not shown"
    )
    print('header link container: ')
    print(e)


# header links: elements (여러 개를 한꺼번에 처리할 때는 무조건 복수형! always return something like [])
@then("Verify 6 links are shown")
def verify_header_link_amount(context):
    links = context.wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")),
        message="Header link container not shown"
    )
    print('header links: ')
    print(links)
    assert len(links) == 6, f'Expected 6 links, but got {len(links)}'