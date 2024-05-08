Feature: Ebay Regression

 Scenario: Search bar Verification
    Given Navigate to ebay.com
    And In search bar type "dress"
    And Click "Search" button
    Then Click the first dress from the page
    And click add to cart
    Then click "go to cart"
    And Item was added to the cart


 Scenario: "Sign in" page is loading verification
    Given Navigate to ebay.com
    And Click "Sign In" button
    Then Verify that "Sign In" page is loaded

 Scenario: "register" page is loading verification
    Given Navigate to ebay.com
    And Click "register" button
    Then Verify that "register" page is loaded

 Scenario: "Daily Deals" page is loading verification
    Given Navigate to ebay.com
    And Click "Daily Deals" button
    Then Verify that "Daily Deals" page is loaded

 Scenario: "Brand Outlet" page is loading verification
    Given Navigate to ebay.com
    And Click "Brand Outlet" button
    Then Verify that "Brand Outlet" page is loaded

  Scenario: "Gift Cards" page is loading verification
    Given Navigate to ebay.com
    And Click "Gift Cards" button
    Then Verify that "Gift Cards" page is loaded

  Scenario: "Help & Contact" page is loading verification
    Given Navigate to ebay.com
    And Click "Help & Contact" button
    Then Verify that "Help & Contact" page is loaded

  Scenario: "Sell" page is loading verification
    Given Navigate to ebay.com
    And Click "Sell" button
    Then Verify that "Sell" page is loaded

  Scenario: After clicking on "Watchlist" button "Sign In" button is displayed
    Given Navigate to ebay.com
    And Click "Watchlist" button
    Then Verify that "Sign In Watchlist" button is displayed

  Scenario: "My eBay" page is loading verification
    Given Navigate to ebay.com
    And Click "My eBay" button
    Then Verify that "My eBay" page is loaded

  Scenario: "My eBay" drop down list is displayed
    Given Navigate to ebay.com
    And Hover over "My eBay" button
    Then Verify that "My eBay" drop down list is displayed

  Scenario: After hover over on "Alert" button "Sign In" button is displayed
    Given Navigate to ebay.com
    And Hover over "Alert" button
    Then Verify that "Sign In Alert" button is displayed

   Scenario: "Cart" page is loading verification
    Given Navigate to ebay.com
    And Click "Cart" button
    Then Verify that "Cart" page is loaded

   Scenario: After hover over on "Cart" button "Your cart is empty" pop up message is displayed
    Given Navigate to ebay.com
    And Hover over "Cart" button
    Then Verify that "Your cart is empty" pop up message is displayed