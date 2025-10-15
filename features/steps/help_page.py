from time import sleep
from behave import given, when, then


@given('Open Help page for Returns')
def open_help_page(context):
    context.app.help_page.open_help_page()


@when('Select Help topic {help_topic}')
def select_promotions(context, help_topic):
    context.app.help_page.select_promotions(help_topic)
    sleep(5)


@then('Verify help {expected_header_text} page opened')
def verify_help_page_opened(context, expected_header_text):
    context.app.help_page.verify_header(expected_header_text)
    sleep(5)