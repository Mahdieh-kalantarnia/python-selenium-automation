
Feature: Tests for search in target

  Scenario Outline: Search for a product
     Given Open target page
     When  Search for <product>
     Then  I should see results to that <product>

     Examples:
     |product  |expected_product |
     |bag      |bag              |
     |watch    |watch            |

