Feature: Tests for search in target

  Scenario Outline: Search for a product
     Given Open target page
     When  Search for <product>
     Then  Add to cart
     Then  Click on add to cart icon
     Then  Click on Continue shopping
     Then  Click on shopping cart icon
     Then  Click on signin to checkout




Examples:
     |product  |           |
     |bag      |           |