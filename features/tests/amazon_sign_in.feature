Feature:   Test for sign in

Scenario:  Verify that a user can click on orders
    Given Open Amazon page
    When Click on orders
    Then Verify Sign in text is Sign in

Scenario: Verify that a user can click on shopping cart
    Given Open Amazon page
    When Click on shopping cart icon
    Then Verify cart result is Your Amazon Cart is empty

Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And Switch back to original
