from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id='addToCartButtonOrTextIdFor12954582'][aria-label*='Add to cart for Tazo Passion Herbal Tea Bags']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "a[data-test='@web/ProductCard/title'][aria-label*='Tazo Passion Herbal']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_RESULT_COUNT_TEXT = (By.CSS_SELECTOR, "span[data-test='text-quill-insert-1']")
    VIEW_CART_AND_CHECK_OUT_BTN = (By.XPATH, "//a[text()='View cart & check out']")

    def verify_search_results(self):
        actual_result = self.find_element(*self.SEARCH_RESULT_COUNT_TEXT)
        assert 'tea' in actual_result, f'Expected tea not in "{actual_result}'

    def search_for_product(self, product):
        search_input = self.find_element(*self.SEARCH_FIELD)

        search_input.send_keys(product)

        self.find_element(*self.SEARCH_BTN).click()

    def verify_product_search_result(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULT_COUNT_TEXT).text
        expected_result = product
        assert expected_result in actual_result, f"Expected {expected_result} but got {actual_result}"
        print(f"Test passed {product}")

    def add_first_product_to_cart(self):
        product = self.find_element(*self.FIRST_PRODUCT)

        self.driver.execute_script("arguments[0].click();", product)

    def click_add_to_cart_button(self):
        button = self.find_element(*self.ADD_TO_CART_BTN)
        self.driver.execute_script("arguments[0].click();", button)

    def click_view_cart_check_out_button(self):
        self.find_element(*self.VIEW_CART_AND_CHECK_OUT_BTN).click()

    def verify_first_product_in_cart(self, product):
        actual_result = self.find_element(*self.CART_ITEM_TITLE).text

        assert actual_result, "No product name found on the cart page."
        print(f"{actual_result}")

    def verify_product_name_and_image(self):
        products = self.find_elements(*self.PRODUCT_CARDS)

        for product in products:
            self.driver.execute_script("arguments[0].scrollIntoView();", product)

            product_title = product.find_element(By.CSS_SELECTOR, "div[title]").text
            assert product_title, 'Product title not shown'
            print(f'🟢{product_title}')
            # product.find_element(*PRODUCT_IMG)

            product_image = product.find_element(By.CSS_SELECTOR, "img[alt]")
            assert product_image, 'Product image not shown'

