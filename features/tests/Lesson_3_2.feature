# Created by Zooni Butt at 8/4/2023
Feature: Test logged out user sees sign-in
  # Enter feature description here

  Scenario: Logged out user sees Sign In when clicking on Returns and Orders
    Given Open amazon
    When Click on Orders
    Then  Verify Sign in page opened

  Scenario: Amazon Cart is empty
    Given Open amazon
    When Click on Cart
    Then  Verify cart is empty