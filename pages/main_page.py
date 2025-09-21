from pages.base_page import Page
from selenium.webdriver.common.by import By
class MainPage(Page):


    ADD_TO_CARD = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    CLICK_ADD_TO_CARD = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def open_main(self):
        self.open_url('https://www.target.com/')

