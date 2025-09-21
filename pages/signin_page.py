

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page

class Signin(Page):

    def verify(self):
        self.url = 'https://www.target.com/login'
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(self.url)
        )
        print("Test passed")