from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on account icon')
def click_cart_icon(context):
  #  context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()
     context.app.header.click_cart_icon()
     sleep(7)


@when('Click on sign in or creat account')
def click_sign_in(context):
    #context.driver.find_element(By.XPATH, "//div/button[@data-test='accountNav-signIn']").click()
    context.app.header.click_sign_in()
    sleep(5)

@then('Verify Sign In form opened')
def verify(context):

    context.app.signin_page.verify()

