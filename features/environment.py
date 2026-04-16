from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
=======
>>>>>>> master


def browser_init(context):
    """
    :param context: Behave context
    """
<<<<<<< HEAD
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
=======
    context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()
>>>>>>> master

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
<<<<<<< HEAD
=======
    context.driver.delete_all_cookies()
>>>>>>> master
    context.driver.quit()
