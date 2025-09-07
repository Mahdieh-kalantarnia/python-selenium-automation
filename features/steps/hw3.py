from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from time import sleep


@given('Open stackoverflow page')
def open_page(context):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/atefehkalantarnia/AppData/Local/Google/Chrome/User Data")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.maximize_window()

    context.driver.get('https://stackoverflow.com/users/signup')
    sleep(5)

@when('the user enters email and password')
def email_password(context):
    context.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("example@yahoo.com")
    context.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345")
    sleep(7)


@when('Click on Sign Up button')
def click_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "#submit-button").click()
    sleep(5)

@then('the user should be registered successfully')
def register(context):
   assert "user" in context.driver.current_url
print("Test Passed: Signup successful")



