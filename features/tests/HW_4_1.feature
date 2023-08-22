# Created by Zooni Butt at 8/4/2023
Feature: Test user sees expected number of links when Best Seller is clicked
  # Enter feature description here

  Scenario: User sees expected number of links when clicks on est Seller
    Given Open amazon
    When Click on Best Seller
    Then  Verify header has expected number of links

