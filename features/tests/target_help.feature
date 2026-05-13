
Feature: Test cases for Target Help page

  Scenario Outline: Verify UI elements on Target Help page
    Given Open Target Help page
    Then Verify <expected_text> text is shown
    Examples:
    |expected_text|
    |Help         |
    |Have a question?|
    |Browse all help |
    |What would you like help with?|
    |Popular Pages                 |

  Scenario: Verify linked 9 cards
    Given Open Target Help page
    Then Verify 9 cards are linked

  Scenario: Verify linked 8 horizontal cards
    Given Open Target Help page
    Then Verify 8 horizontal cards are linked

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

    # make topic options dynamic scenario
  Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened

  Scenario: User can select Help topic on Returns page
    Given Open Help page for Returns
    When Select Help topic Orders & Purchases
    Then Verify help Print a receipt page opened

