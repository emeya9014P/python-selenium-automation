# Created by emeya at 4/25/2026
Feature: Test cases for header

  Scenario: Verify user sees header links
    Given Open Target main page
    Then Verify header link container is shown
    Then Verify 6 links are shown

  Scenario: User can Sign in
    Given Open Target main page
    When Click Account button
    Then Verify sign in button opened

