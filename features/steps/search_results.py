from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULT_COUNT_TEXT = (By.CSS_SELECTOR, "span[data-test='text-quill-insert-1']")


@then("Verify search result for {product} shown")
def verify_search_result_for_tea(context, product):
    actual_result = context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
    sleep(3)
    expected_result = product
    assert expected_result in actual_result
    print("Test passed")


# @given("Open Target main page")
# def open_main_page(context):
#     context.driver.get("https://target.com")
#     sleep(3)


# @when("Search for tea")
# def search_for_tea(context):
#     context.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
#     sleep(3)


@when ("Click on the first product")
def click_add_to_cart_button(context):
    product = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/ProductCard/title'] div[title='Tazo Passion Herbal Tea Bags - 20ct']")
    sleep(2)
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)
    sleep(2)
    product.click()
    sleep(2)


@when ("Click on Add to cart button")
def click_add_to_cart_button_in_side_panel(context):
    button = context.driver.find_element(By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor12954582'][aria-label*='Add to cart for Tazo Passion Herbal Tea Bags']")
    sleep(2)
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    sleep(2)
    button.click()
    sleep(2)


@when ("Click View cart & check out button")
def click_view_cart_check_out_button(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    sleep(3)


@then("Verify the product is in the cart")
def verify_product_in_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[contains(text(), 'Tazo Passion Herbal Tea Bags')]").text
    assert 'Tazo Passion' in actual_result, f"Expected Tazo Passion, but got {actual_result}"
    print("Test Passed: Product is in the cart!")