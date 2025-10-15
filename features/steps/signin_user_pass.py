from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




PASS_ICON=(By.XPATH,"//div[@id='password']")
PASSWORD=(By.ID, 'password')
SIGNIN_BTN=(By.XPATH,"//button[text()='Sign in with password']")

@then('Enter your email adress')
def enter_email(context):
   context.app.signin_page.enter_the_email()
sleep(3)


@then('Click on continue btn')
def click_continue(context):
    context.app.signin_page.continue_btn()
    sleep(3)

@then('Click on enter password icon')
def click_enter_password(context):
    context.app.signin_page.password_icon()
    sleep(3)

@then('Enter your password')
def enter_password(context):
    context.app.signin_page.password_enter()
    sleep(3)

@then('Click on signin btn')
def click_signin(context):
    context.app.signin_page.signin_btn()
    sleep(3)

@then('Verify the msg Please enter a valid password')
def verify_msg(context):
    context.app.signin_page.verify_message()

