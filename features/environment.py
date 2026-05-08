from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=10)

    context.app = Application(context.driver)

## HEADLESS MODE #### meaning test without interface
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# context.driver = webdriver.Chrome(
#     options=options
# )

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.quit()


########### BROWSERSTACK Code ####################
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# from app.application import Application
#
# def browser_init(context):
#     """
#     :param context: Behave context
#     """
#
# def before_scenario(context, scenario):
#     # 1. 브라우저스택 설정
#     bstack_options = {
#         "os": "Windows",
#         "osVersion": "11",
#         "browserName": "Chrome",
#         "browserVersion": "latest",
#         "userName": "ChanUserName",
#         "accessKey": "ChanAccessKey",
#         "sessionName": scenario.name,
#         "buildName": "Test_Build_01",
#         "projectName": "My_First_Target_Test",
#         "local": "false"
#     }
#
#     options = ChromeOptions()
#     options.set_capability('bstack:options', bstack_options)
#     bs_url = f"https://{bstack_options['userName']}:{bstack_options['accessKey']}@hub-cloud.browserstack.com/wd/hub"
#
#     # 원격 브라우저 실행
#     context.driver = webdriver.Remote(
#         command_executor=bs_url,
#         options=options
#     )
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(5)
#
#     context.app = Application(context.driver)
#
#     context.wait = WebDriverWait(context.driver, timeout=15)
#
# def after_scenario(context, scenario):
#     context.driver.quit()
