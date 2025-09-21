Feature: Tests for sign in  icon

  Scenario: User can click on account icon
    Given Open target page
    When  Click on account icon
    And   Click on sign in or creat account
    Then  Verify Sign In form opened

