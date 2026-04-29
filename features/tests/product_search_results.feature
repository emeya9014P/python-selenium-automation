
# Created by Svetlana at 4/4/19

#Feature: Test Scenarios for Search functionality
#
#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    And Click on search icon
#    Then Product results for Car are shown

Feature: Test cases for Product Search on Target

  Scenario: Use can search for a product "tea" on Target
    Given Open Target main page
    When Search for tea
    Then Verify search result for tea shown

  Scenario: Use can search for a product "coffee" on Target
    Given Open Target main page
    When Search for coffee
    Then Verify search result for coffee shown

# data driven
  Scenario Outline: User can search for products
    Given Open Target main page
    When Search for <search_query>
    Then Verify search result for <product> shown
    Examples:
    |search_query | product |
    |tea          | tea     |
    |coffee       | coffee  |
    |gum          | gum     |

  Scenario: After search, add any product into the cart and verify it is there
    Given Open Target main page
    When Search for tea
    And Click on the first product
    And Click on Add to cart button
    And Click View cart & check out button
    Then Verify the product is in the cart