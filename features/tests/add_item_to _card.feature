Feature: Tests for search in target

  Scenario Outline: Search for a product
     Given Open target circle page
     When  Search for <product>
     Then  I should see results to that <product>
     Then  Add to cart
     Then  Click on cart icon
     Then  Click on Continue shopping
     Then  Click on shopping cart
     Then  Click on signin to checkout

       Examples:
     |product        |expected_product |
     |mug         |mug        |



