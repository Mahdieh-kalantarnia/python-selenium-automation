
from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product A-94628520 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/women-s-balloon-long-sleeve-v-neck-blouse-universal-thread/-/A-94628520?preselect=94604887#lnk=sametab')
    sleep(5)


@then('User can click choosr a  color')
def click_and_verify_colors(context):
    expected_colors = ['Black','White']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for c in colors:
        c.click()
        sleep(1)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'