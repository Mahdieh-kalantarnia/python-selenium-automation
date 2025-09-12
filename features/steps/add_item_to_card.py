from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BOX=(By.ID, 'search')
SEARCH_BTN=(By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CARD=(By.CSS_SELECTOR, "[id*='addToCartButton']")

ADD_CARD2=(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
CONTINUE_SHOPPING=(By.XPATH,"(//button[normalize-space()='Continue shopping'])[1]")
SHOPPING_CART=(By.XPATH,'//a[@data-test="@web/CartLink"]')

@then('Add to cart')
def add_item_to_cart(context):
    context.driver.find_element(*ADD_TO_CARD).click()
    sleep(5)

@then('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*ADD_CARD2).click()
    sleep(5)


@then('Click on Continue shopping')
def click_cart_icon(context):
    context.driver.find_element(*CONTINUE_SHOPPING).click()
    sleep(5)


@then('Click on shopping cart')
def click_shopping_cart(context):
    context.driver.find_element(*SHOPPING_CART).click()
    sleep(5)


@then('Click on signin to checkout')
def click_shopping_cart(context):
    context.driver.find_element(By.XPATH,'//button[(@ data-test="checkout-button" and text()="Sign in to check out")]').click()
    sleep(5)
