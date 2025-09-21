from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CARD = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    CLICK_ADD_TO_CARD = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    CONTINUE_SHOPPING = (By.XPATH, "(//button[normalize-space()='Continue shopping'])[1]")

    def verify_search_results(self, product):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CARD).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.CLICK_ADD_TO_CARD).click()

    def Continue_shopping_btn(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()