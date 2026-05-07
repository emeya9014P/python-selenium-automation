from behave import given, when, then

@given ("Open Target App page")
def open_target_app_page(context):
    context.app.target_app_page.open_target_app_page()


@given ("Store original window")
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()
    print('original_window', context.original_window)

    # All windows:
    # print('All windows', context.driver.window_handles)


@when ("Click Privacy Policy link")
def click_privacy_policy_link(context):
    context.app.target_app_page.click_pp_link()
    print('All windows', context.driver.window_handles)
    print('current_window', context.driver.current_window_handle)


@when ("Switch to new window")
def switch_window(context):
    context.app.base_page.switch_to_new_window()

    # all_windows = context.driver.window_handles
    # context.driver.switch_to.window(all_windows[1])
    # print('current_window', context.driver.current_window_handle)


@then ("Verify Privacy Policy page opened")
def verify_pp_page_opened(context):
    context.app.privacy_policy_page.verify_pp_page_opened()


@then ("Close current page")
def close_current_page(context):
    context.app.base_page.close_window()

    # context.driver.close()
    # print('All windows after closing privacy policy window', context.driver.window_handles)


@then ("Return to original window")
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)
    print('Current window after returning', context.driver.current_window_handle)

