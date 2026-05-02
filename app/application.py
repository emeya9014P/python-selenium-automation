from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header_page import Header
from pages.main_page import MainPage
from pages.product_details_page import ProductDetailsPage
from pages.product_search_results_page import SearchResultsPage
from pages.target_circle_page import TargetCirclePage
from pages.target_help_page import TargetHelpPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header_page = Header(driver)
        self.main_page = MainPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.product_search_results_page = SearchResultsPage(driver)
        self.target_circle_page = TargetCirclePage(driver)
        self.target_help_page = TargetHelpPage(driver)



