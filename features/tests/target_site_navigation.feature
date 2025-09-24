Feature: User can open and close Terms and Conditions from sign in page


  Scenario: User is able to open Privacy Policy
     Given Open sign in page
     And   Store original window
     When  Click on Target terms and conditions link
     And   Switch to new window
     Then  Verify Privacy Policy page opened
     And   Close current page
     And   Return to original window