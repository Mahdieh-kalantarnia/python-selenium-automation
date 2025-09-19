from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target page')
def open_target(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()
    sleep(5)

@when('Click on cart icon')
def click_cart_icon(context):

    context.app.header.click_cart()
    sleep(7)

@then('Verify the message is shown')
def message(context):


   context.app.cart_page.verify_cart_empty_msg()
   sleep(5)
