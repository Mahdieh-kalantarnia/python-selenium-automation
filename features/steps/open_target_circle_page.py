from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target circle page')
def target_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(5)
