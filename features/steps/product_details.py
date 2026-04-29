from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
    sleep(5)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        # for visibility only:
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@given('Open target product A-1000044024 page')
def open_target(context):
    context.driver.get(
            f'https://www.target.com/p/wrangler-workwear-men-s-long-sleeve-heavyweight-pocket-t-shirt-size-s-5xl/-/A-1000044024?preselect=94177950#lnk=sametab')

    context.wait.until(
        EC.presence_of_element_located((By.ID, 'search')),
        message=f'Target product page is not opened'
    )

@then('Verify user can click through available colors')
def click_and_verify_colors(context):
    expected_colors = ['black', 'duck', 'monument', 'redwood']
    actual_colors = []

    colors = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] img")  # [webelement1, webelement2, webelement3]
    print(colors)

    for c in colors:
        c.click()
        # for visibility only:
        sleep(0.1)

        selected_color = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/VariationComponent']")[1].text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
