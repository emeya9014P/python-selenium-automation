from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# COLOR_OPTIONS = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] img")
# SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
COLOR_OPTIONS = (By.XPATH, "//div[@data-test='@web/VariationComponent'][.//span[contains(text(), 'Color') or contains(text(), 'color')]]//img")
SELECTED_COLOR = (By.XPATH, "//div[@data-test='@web/VariationComponent'][.//span[contains(text(), 'Color') or contains(text(), 'color')]]//div[contains(@class, 'styles_headerWrapper')]")

PRODUCT_URL_A91269718 = 'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab'
PRODUCT_URL_A1000044024 = 'https://www.target.com/p/wrangler-workwear-men-s-long-sleeve-heavyweight-pocket-t-shirt-size-s-5xl/-/A-1000044024?preselect=94177950#lnk=sametab'


@given('Open target product A-91269718 page')
def open_a91269718_step(context):
    context.app.product_details_page.open_a91269718_page()


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    context.app.product_details_page.click_and_verify_a91269718_colors()


@given('Open target product A-1000044024 page')
def open_a1000044024_step(context):
    context.app.product_details_page.open_a1000044024_page()


@then('Verify user can click through available colors')
def click_and_verify_colors(context):
    context.app.product_details_page.click_and_verify_a1000044024_colors()
