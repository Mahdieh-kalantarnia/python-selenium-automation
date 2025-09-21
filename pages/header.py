
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page



class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    ACCOUNT_ICON = (By.CSS_SELECTOR, "#account-sign-in")
    CREATE_ACCOUNT_BTN=(By.XPATH,  "//div/button[@data-test='accountNav-signIn']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(9)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_cart_icon(self):
        self.driver.find_element(*self.ACCOUNT_ICON).click()

    def click_sign_in(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_BTN).click()