# Created by emeya at 5/3/2026
Feature: Test cases for sign-in page

#  Scenario: User can open and close Terms and Conditions page from sign in page
#    Given Open Target main page
#    When Click Account button
#    When From right side navigation menu, click Sign In
#    When Store original window
#    And Click on Target Terms and Conditions link
#    And Switch to the newly opened window
#    Then Verify Terms and Conditions page is opened
#    And User can close new window
#    And Switch to original page

  Scenario: User can verify error message when incorrect password was entered
    Given Open Target main page
    When Click Account button
    When From right side navigation menu, click Sign In
    When Enters correct email, 'test_user@example.com'
    Then Click on Continue button
    When Click Enter your password button
    When Enters incorrect password, '12oqqoQ!'
    Then Click Sign in with password
    Then Verifies that an error message is shown
