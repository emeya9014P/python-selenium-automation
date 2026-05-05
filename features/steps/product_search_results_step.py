from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor12954582'][aria-label*='Add to cart for Tazo Passion Herbal Tea Bags']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/title']")
FIRST_PRODUCT = (By.CSS_SELECTOR, "a[data-test='@web/ProductCard/title'][aria-label*='Tazo Passion Herbal']")
PRODUCT_CARDS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
SEARCH_RESULT_COUNT_TEXT = (By.CSS_SELECTOR, "span[data-test='text-quill-insert-1']")
VIEW_CART_AND_CHECK_OUT_BTN = (By.XPATH, "//a[text()='View cart & check out']")

# tea, coffee, scenario outline 시나리오 모두 포함`
@then("Verify search result for {product} shown")
def verify_search_result_for_product(context, product):
    context.app.product_search_results_page.verify_product_search_result(product)


@then("Verify URL has searchTerm={product}")
def verify_url_product(context, product):
    context.app.product_search_results_page.verify_url_product(product)


@when ("Click on the first product")
def click_add_to_cart_button(context):
    context.app.product_search_results_page.add_first_product_to_cart()


@when ("Click on Add to cart button")
def click_add_to_cart_button(context):
    context.app.product_search_results_page.click_add_to_cart_button()


@when ("Click View cart & check out button")
def click_view_cart_check_out_button(context):
    context.app.product_search_results_page.click_view_cart_check_out_button()


@then("Verify the {product} is in the cart")
def verify_product_in_cart(context, product):
    context.app.product_search_results_page.verify_first_product_in_cart(product)


@then("Verify that every product has a name and an image")
def verify_product_name_and_image(context):
    context.app.product_search_results_page.verify_product_name_and_image()
