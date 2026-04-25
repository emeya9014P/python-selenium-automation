# Created by emeya at 4/24/2026
#2. Create a test case using BDD that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown:
#Open target.com
#Click on Cart icon
#Verify “Your cart is empty” message is shown

Feature: Test case to click on the cart icon and verify 'Your cart is empty' in Target.com
  # Enter feature description here

  Scenario: user can confirm 'Your cart is empty' message
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown