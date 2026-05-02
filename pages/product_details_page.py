from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ProductDetailsPage(Page):
    # COLOR_OPTIONS = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] img")
    # SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

    COLOR_OPTIONS = (By.XPATH, "//div[@data-test='@web/VariationComponent'][.//span[contains(text(), 'Color') or contains(text(), 'color')]]//img")
    SELECTED_COLOR = (By.XPATH,"//div[@data-test='@web/VariationComponent'][.//span[contains(text(), 'Color') or contains(text(), 'color')]]//div[contains(@class, 'styles_headerWrapper')]")
    PRODUCT_URL_A91269718 = 'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab'
    PRODUCT_URL_A1000044024 = 'https://www.target.com/p/wrangler-workwear-men-s-long-sleeve-heavyweight-pocket-t-shirt-size-s-5xl/-/A-1000044024?preselect=94177950#lnk=sametab'


    def open_a91269718_page(self):
        self.driver.get(self.PRODUCT_URL_A91269718)
        sleep(5)


    def click_and_verify_a91269718_colors(self):
        sleep(5)

        expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
        actual_colors = []

        colors = self.driver.find_elements(*self.COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
        print(colors)

        for c in colors:
            c.click()
            # for visibility only:
            sleep(0.5)

            selected_color = self.driver.find_element(*self.SELECTED_COLOR).text  # 'Color\nBlack'
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


    def open_a1000044024_page(self):
        self.driver.get(self.PRODUCT_URL_A1000044024)
        sleep(5)


    def click_and_verify_a1000044024_colors(self):
        sleep(5)

        expected_colors = ['black', 'duck', 'monument', 'redwood']
        actual_colors = []

        colors = self.driver.find_elements(*self.COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
        print(colors)

        for c in colors:
            c.click()
            # for visibility only:
            sleep(0.5)

            selected_color = self.driver.find_element(*self.SELECTED_COLOR).text  # 'Color\nBlack'
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


