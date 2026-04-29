from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    actual_result = context.wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Your cart is empty']")),
        message='"Your cart is empty" message is not shown'
    )
    expected_result = 'Your cart is empty'
    assert 'Your cart is empty' in actual_result.text
    print("Test Passed")

