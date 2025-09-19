Feature: “Your cart is empty” message is shown for empty cart

  Scenario: Successful message is shown for empty cart
    Given Open target page
    When Click on cart icon
    Then Verify the message is shown


