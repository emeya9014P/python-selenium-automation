# Created by emeya at 4/24/2026
#3. Create a test case using BDD to verify that a logged out user can navigate to Sign In:
#Open target.com
#Click Sign In
#From right side navigation menu, click Sign In
#Verify Sign In form opened

Feature: Test case to verify a logged out user can navigate to sign in in Target.com

Scenario: User can Sign in
  Given Open Target main page
  When Click Account button
  Then Verify sign in button opened
    # Enter steps here

