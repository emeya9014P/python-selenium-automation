from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT_BTN = (By.CSS_SELECTOR, "#account-sign-in")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")
HEADER_LINKS_CONTAINER = (By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
SEARCH_FIELD = (By.ID, 'search')
SIGN_IN_BTN_SIDE_NAV = (By.XPATH, "//button[contains(text(),'Sign in')]")


@when("Click on Cart icon")
def click_cart_icon(context):
    context.app.header_page.click_cart()
    # self.wait_until_clickable(*self.CART_ICON)

@when("Click Account button")
def click_account(context):
    context.app.header_page.click_account_btn()


@when("From right side navigation menu, click Sign In")
def click_sign_in_navigation_menu(context):
    context.app.header_page.click_sign_in_navigation_menu()


@then("Verify Sign in form opened")
def verify_signin_form_open(context):
    context.app.header_page.verify_signin_form_opened()


@when ("Click Sign In button")
def click_sign_in_button(context):
    context.app.header_page.click_sign_in_button()


# tea, coffee, scenario outline 시나리오 모두 포함
@when("Search for {product}")
def search_for_product(context, product):
    context.app.product_search_results_page.search_for_product(product)


# header link: element
@then("Verify header links container is shown")
def verify_header_links_container_shown(context):
    context.app.header_page.verify_header_links_container_shown()


# header links: elements (여러 개를 한꺼번에 처리할 때는 무조건 복수형! always return something like [])
@then("Verify 6 links are shown")
def verify_header_links_count(context):
    context.app.header_page.verify_header_links_count()
