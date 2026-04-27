# Created by emeya at 4/26/2026
Feature: Target Help page test cases
  # Enter feature description here

#  Scenario: Verify UI elements on Target Help page
#    Given Open Target Help page
#    Then Verify Help text is shown

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

