Feature: Check Benefit Cards on Target Website

  Scenario: Verify at least 10 Benefit cards are present
    Given Open target circle page
    When  I look at the Benefit cards section
    Then  Verify benefit cards

