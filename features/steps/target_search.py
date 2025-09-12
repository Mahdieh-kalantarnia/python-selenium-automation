
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BOX=(By.ID, 'search')
SEARCH_BTN=(By.XPATH,"//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")


@when('Search for {search_word}')
def search(context, search_word):
    context.driver.find_element(*SEARCH_BOX).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(7)

@then('I should see results to that {product}')
def verify_results(context, product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    assert product in actual_text, f'Error.{product} Not Found! {product} Actual_text: {actual_text}'
    sleep(5)



