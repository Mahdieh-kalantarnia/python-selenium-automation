
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class Signin(Page):
    EMAIL_ADD = (By.ID, 'username')
    CONTINUE_BTN = (By.XPATH, "//button[@id='login']")
    PASS_ICON = (By.XPATH, "//div[@id='password']")
    PASSWORD = (By.ID, 'password')
    SIGNIN_BTN = (By.XPATH, "//button[text()='Sign in with password']")


    def verify(self):
        self.url = 'https://www.target.com/login'
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.url)
        )
        print("Test passed")


    def enter_the_email(self):
        self.driver.find_element(*self.EMAIL_ADD).send_keys('atefeh210@yahoo.com')


    def continue_btn(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def password_icon(self):
        self.driver.find_element(*self.PASS_ICON).click()

    def password_enter(self):
        self.driver.find_element(*self.PASSWORD).send_keys('1234')

    def signin_btn(self):
        self.driver.find_element(*self.SIGNIN_BTN).click()

    def verify_message(self):
        assert "Please enter a valid password" in self.context.driver.find_element(By.TAG_NAME,"body").text, "Test not passed"

        print("Test passed")