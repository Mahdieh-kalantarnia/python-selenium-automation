from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given("I open the Target Help page")
def step_open_help_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/help")

@then("I should see the search box")
def step_see_search_box(context):
    search_box = context.driver.find_element(By.ID, "helpSearch")
    assert search_box.is_displayed(), "Search box not visible"

@then("I should see the header logo")
def step_see_header_logo(context):
    header_logo = context.driver.find_element(By.CSS_SELECTOR, "#headerPrimary")
    assert header_logo.is_displayed(), "Logo not visible"

@then("I should see the help categories")
def step_see_help_categories(context):
    categories = context.driver.find_elements(By.XPATH, '//div/a[@class="styles_ndsLink__GUaai styles_onLight__QKcK7 sc-f27d6425-0 icMhKd sc-a73ee9a2-1 dUvdtI"]')
    assert len(categories) > 0, "No categories found"

