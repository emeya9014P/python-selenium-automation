class Page: # base page = abstraction

    def click(self):
        print('Clicking')

    def input_text(self, text):
        print('Inputting text')

    def find_element(self):
        print('Searching for....')

class MainPage(Page):
    # locators
    def open_main(self):
        print('Opening.... ')

class Login(Page):
    def login(self):
        print('Logging in as ....')

login_page = Login()
login_page.input_text('test')