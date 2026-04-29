from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULT_COUNT_TEXT = (By.CSS_SELECTOR, "span[data-test='text-quill-insert-1']")


@then("Verify search result for {product} shown")
def verify_search_result_for_tea(context, product):

    element = context.wait.until(
        EC.visibility_of_element_located((SEARCH_RESULT_COUNT_TEXT)),
        message="Search result for {product} not shown"
    )
    actual_result = element.text
    expected_result = product
    assert expected_result in actual_result
    print("Test passed")


@when ("Click on the first product")
def click_add_to_cart_button(context):
    product = context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='@web/ProductCard/title'] div[title='Tazo Passion Herbal Tea Bags - 20ct']")),
        message="First product is unclickable"
    )
    context.driver.execute_script("arguments[0].click();", product)
# use when banner covers product
# context.driver.execute_script("arguments[0].click();", product)


@when ("Click on Add to cart button")
def click_add_to_cart_button_in_side_panel(context):
    button = context.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor12954582'][aria-label*='Add to cart for Tazo Passion Herbal Tea Bags']")),
        message="Add to cart button is unclickable"
    )
    context.driver.execute_script("arguments[0].click();", button)


@when ("Click View cart & check out button")
def click_view_cart_check_out_button(context):
    button = context.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='View cart & check out']")),
        message="View cart & check out button is unclickable"
    )
    button.click()


@then("Verify the product is in the cart")
def verify_product_in_cart(context):
    element = context.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Tazo Passion Herbal Tea Bags')]")),
        message="Product is not found"
    )

    actual_result = element.text
    assert 'Tazo Passion' in actual_result, f"Expected Tazo Passion, but got {actual_result}"
    print("Test Passed: Product is in the cart!")

# EC examples:
# context.wait.until(EC.visibility_of_element_located(SIDE_NAV_ADD_TO_CART_BTN))
# @when('Confirm Add to Cart button from side navigation')
# def side_nave_click_to cart(context):
#     context.wait.until(
#         EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
#         message='Add to Cart button from side navigation not visible'
# ).click()
#     context.wait.until(
#         EC.visibility_of_element_located(ADDED_TO_CART_TXT),
#         message='Added to cart text not shown'
#     )