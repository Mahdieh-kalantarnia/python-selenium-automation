from  behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_target_page(context):
    context.app.target_login_page.open_target_navigation()
    sleep(2)


@given('Store original window')
def store_window(context):
    context.original_window = context.app.page.get_original_window()
    print('Original window: ', context.original_window)
    sleep(2)


@when('Click on Target terms and conditions link')
def click_privacy_link(context):
    context.app.target_login_page.click_privacy_link()
    sleep(2)


@when('Switch to new window')
def switch_window(context):
    # current_windows = context.driver.window_handles
    # print('Current windows after link click: ', current_windows) # [Win1, Win2...]
    # new_window = current_windows[1]
    # print('New window: ', new_window)
    # context.driver.switch_to.window(new_window)
    context.app.page.switch_to_newly_opened_window([context.original_window])



@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_privacy_opened()



@then('Close current page')
def close_page(context):
    context.app.page.close()
    sleep(2)


@then('Return to original window')
def switch_to_original_window(context):
    # context.driver.switch_to.window(context.original_window)
    # print('Switching back to: ', context.original_window)
    context.app.page.switch_to_window_by_id(context.original_window)
    sleep(2)