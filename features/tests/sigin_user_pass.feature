Feature: Tests for sign in  icon with user and password

  Scenario: User can click on account icon
    Given Open target page
    When  Click on account icon
    And   Click on sign in or creat account
    Then  Enter your email adress
    And  Click on continue btn
    Then Click on enter password icon
    Then Enter your password
    Then Click on signin btn
    Then Verify the msg Please enter a valid password
