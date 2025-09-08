Feature:Test Scenarios for Stackoverflow Singup

  Scenario: Successful signup with email and password
    Given Open stackoverflow page
    When the user enters email and password
    And  Click on Sign Up button
    Then the user should be registered successfully
