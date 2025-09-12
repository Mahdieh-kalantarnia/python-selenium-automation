
from time import sleep
from behave import given, when, then

from selenium.webdriver.common.by import By


@when('I look at the Benefit cards section')
def step_look_benefit_section(context):
    context.benefit_cards =context.driver.find_elements(
        By.XPATH,"//div[contains(@data-component-audience, 'null') or contains(@data-component-audience, 'control')]"
    )
    sleep(5)


@then('Verify benefit cards')
def verify_benefit_cards(context):
    print(f"Benefit cards found: {len(context.benefit_cards)}")
    assert len(context.benefit_cards) >= 10, f"Expected at least 10 cards, but found {len(context.benefit_cards)}"
