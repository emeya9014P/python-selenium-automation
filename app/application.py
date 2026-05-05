from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header_page import Header
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.product_details_page import ProductDetailsPage
from pages.product_search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.target_circle_page import TargetCirclePage
from pages.target_help_page import TargetHelpPage
from pages.terms_and_conditions_page import TermsAndConditionsPage
from pages.sign_in_page import SignInPage



class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.header_page = Header(driver)
        self.main_page = MainPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.product_search_results_page = SearchResultsPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.target_circle_page = TargetCirclePage(driver)
        self.target_help_page = TargetHelpPage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)
        self.sign_in_page = SignInPage(driver)


