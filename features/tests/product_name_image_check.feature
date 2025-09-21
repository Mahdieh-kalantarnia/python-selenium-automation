Feature: Each product should have a name and an image on Target search results

Scenario Outline:Check name and an image
    Given Open target page
    When  Search for <product>
    Then Every product on the search results page should have
       Examples:
     |product        |       |
     |blouse         |       |

