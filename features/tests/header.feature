# Created by emeya at 4/25/2026
Feature: Test cases for header

  Scenario: Verify user sees header links
    Given Open Target main page
    Then Verify header links container is shown
    Then Verify 6 links are shown

  Scenario: Verify user can Sign in
    Given Open Target main page
    When Click Account button
    When From right side navigation menu, click Sign In
    Then Verify Sign in form opened

#  Scenario: Verify user is logged in
#    Given Open Target main page
#    When Click Account button
#    When From right side navigation menu, click Sign In
#    When Enter your password and Sign in with password button
#    Then Verify user is logged in




