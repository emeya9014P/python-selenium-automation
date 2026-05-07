from pages.base_page import BasePage

class PrivacyPolicyPage(BasePage):

    def verify_pp_page_opened(self):
        self.wait_until_url_contains('target-privacy-policy')

# Commit test