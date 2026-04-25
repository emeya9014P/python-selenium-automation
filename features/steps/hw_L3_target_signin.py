from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open target.com")
def open_target_main(context):
    context.driver.get("https://target.com")
    sleep(3)


@when("Click Account button")
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
    sleep(3)


@then("Verify sign in button opened")
def verify_signin_button_open(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").text
    expected_result = "Sign in or create account"
    actual_result = context.driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").text
    assert "Sign in or create account" in actual_result
    print("Test passed")
