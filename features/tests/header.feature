# Created by emeya at 4/25/2026
Feature: Tests for header

  Scenario: Verify user sees header links
    Given Open Target main page
    Then Verify header link container is shown
    Then Verify 6 links are shown

