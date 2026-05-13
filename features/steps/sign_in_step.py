from behave import given, when, then


@when("Store original window")
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()
    print('original_window', context.original_window)


@when("Click on Target Terms and Conditions link")
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_tp_link()


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()


@then("Verify Terms and Conditions page is opened")
def verify_terms_and_conditions_page_opened(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page_opened()


@then("User can close new window")
def close_current_page(context):
    context.app.base_page.close_window()


@then("Switch to original page")
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)


@when("Enters correct email, 'test_user@example.com'")
def enter_correct_email(context):
    context.app.sign_in_page.enter_correct_email(email='dawaja1146@inreur.com')


@then("Click on Continue button")
def click_continue_btn(context):
    context.app.sign_in_page.click_continue_btn()


@when("Click Enter your password button")
def click_enter_your_password_btn(context):
    context.app.sign_in_page.enter_your_password_btn()


@when("Enters incorrect password, '12oqqoQ!'")
def enter_incorrect_password(context):
    context.app.sign_in_page.enter_incorrect_password(password='12oqqoQ!')


@then("Click Sign in with password")
def click_sign_in_with_password_btn(context):
    context.app.sign_in_page.click_sign_in_with_password_btn()


@then("Verifies that an error message is shown")
def verify_error_message(context):
    context.app.sign_in_page.verify_error_message()
