# Created by emeya at 4/25/2026
Feature: Test cases for header

  Scenario: Verify user sees header links
    Given Open Target main page
    Then Verify header links container is shown
    Then Verify 6 links are shown

  Scenario: Verify user can Sign in
    Given Open Target main page
    When Click Account button
    Then Verify signin button opened

