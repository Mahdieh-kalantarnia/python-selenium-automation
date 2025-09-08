from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartLink']").click()
    sleep(7)

@then('Verify the message is shown')
def message(context):
   assert "cart" in context.driver.current_url
print("Test Passed:Your cart is empty ")
