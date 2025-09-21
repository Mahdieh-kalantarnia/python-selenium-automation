from selenium.webdriver.common.by import By


from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    SHOPPING_CART = (By.XPATH, '//a[@data-test="@web/CartLink"]')
    SIGNIN_TO_CHECKOUT = (By.XPATH, '//button[(@ data-test="checkout-button" and text()="Sign in to check out")]')

    def verify_cart_empty_msg(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)


    def shopping_cart_icon(self):
        self.driver.find_element(*self.SHOPPING_CART).click()


    def signin_to_checkout_btn(self):
        self.driver.find_element(*self.SIGNIN_TO_CHECKOUT).click()

