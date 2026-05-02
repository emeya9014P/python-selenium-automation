from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
ACCOUNT_BTN = (By.CSS_SELECTOR, "#account-sign-in")
SIGN_IN_BTN_SIDE_NAV = (By.XPATH, "//button[contains(text(),'Sign in')]")
HEADER_LINKS_CONTAINER = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")
HEADER_LINKS = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")

@when("Click on Cart icon")
def click_cart_icon(context):
    context.app.header_page.click_cart()


@when("Click Account button")
def click_account(context):
    context.app.header_page.click_account_btn()


@then("Verify signin button opened")
def verify_signin_button_open(context):
    context.app.header_page.verify_signin_button_opened()


# tea, coffee, scenario outline 시나리오 모두 포함
@when("Search for {product}")
def search_for_product(context, product):
    context.app.product_search_results_page.search_for_product(product)


# @when("Search for tea")
# def search_for_tea(context):
#     context.driver.find_element(*SEARCH_FIELD).send_keys("tea")
#     context.driver.find_element(*SEARCH_BTN).click()
#     sleep(3)


# header link: element
@then("Verify header links container is shown")
def verify_header_links_container_shown(context):
    context.app.header_page.verify_header_links_container_shown()


# header links: elements (여러 개를 한꺼번에 처리할 때는 무조건 복수형! always return something like [])
@then("Verify 6 links are shown")
def verify_header_links_count(context):
    context.app.header_page.verify_header_links_count()
