Feature: Ebay Regression

 Scenario: Search bar Verification
    Given Navigate to "ebay.com"
    And In search bar type "dress"
    And Click the "Search" button
    Then Click the first dress from the page
    And click add to cart
    #Then click "go to cart"
    #And Item was added to the cart


 Scenario: "Sign in" page is loading verification
    Given Navigate to "ebay.com"
    And Click the "Sign In" button
    Then Verify that "Sign In" page is loaded

 Scenario: "register" page is loading verification
    Given Navigate to "ebay.com"
    And Click the "register" button
    Then Verify that "register" page is loaded

  Scenario Outline: page loading verification
    Given Navigate to "ebay.com"
    And Click "<button_name>" button
    Then Verify that "<page_title>" page is loaded with title

    Examples:
    |button_name|page_title|
    | Daily Deals|Daily Deals|
    | Brand Outlet|Brand Outlet|
    | Gift Cards|Gift Cards|
    | Help & Contact|Help & Contact|
    | Sell|Sell|


  Scenario: After clicking on "Watchlist" button "Sign In" button is displayed
    Given Navigate to "ebay.com"
    And Click the "Watchlist" button
    Then Verify that "Sign In Watchlist" button is displayed

  Scenario: "My eBay" page is loading verification
    Given Navigate to "ebay.com"
    And Click the "My eBay" button
    Then Verify that "My eBay" page is loaded

  Scenario: "My eBay" drop down list is displayed
    Given Navigate to "ebay.com"
    And Hover over "My eBay" button
    Then Verify that "My eBay" drop down list is displayed

  Scenario: After hover over on "Alert" button "Sign In" button is displayed
    Given Navigate to "ebay.com"
    And Hover over "Alert" button
    Then Verify that "Sign In Alert" button is displayed

  Scenario: "Cart" page is loading verification
    Given Navigate to "ebay.com"
    And Click the "Cart" button
    Then Verify that "Cart" page is loaded

  Scenario: After hover over on "Cart" button "Your cart is empty" pop up message is displayed
    Given Navigate to "ebay.com"
    And Hover over "Cart" button
    Then Verify that "Your cart is empty" pop up message is displayed

  Scenario: Filter validation for style
    Given Navigate to "ebay.com"
    And In search bar type "dress"
    And Click the "Search" button
    Then Style filter "Pattern" by "Solid"

  Scenario: Filter validation for size
    Given Navigate to "ebay.com"
    And In search bar type "dress"
    And Click the "Search" button
    Then Size filter "Junior" for "Juniors Size" and "XS"

  Scenario: Filter validation for Color
    Given Navigate to "ebay.com"
    And In search bar type "dress"
    And Click the "Search" button
    Then Choose "Black" color

  Scenario: Filter validation for Buying format or Item Location
    Given Navigate to "ebay.com"
    And In search bar type "dress"
    And Click the "Search" button
    Then in "Item Location" click "US Only"

  Scenario Outline: Search validation
    Given Navigate to "ebay.com"
    And In search bar type "<our_search1>"
    Then all items are "<our_search1>" related

    Examples:
      | our_search1 |
      | dress       |
      | iphone      |
      | samsung     |

  Scenario Outline: Search validation on X pages
    Given Navigate to "ebay.com"
    And In search bar type "<our_search2>"
    And Click the "Search" button
    Then all items are "<our_search2>" related on "<page_quantity1>" amount of pages

    Examples:
      | our_search2 | page_quantity1 |
      | dress       | 2              |
      | iphone      | 3              |
      | samsung     | 3              |


  Scenario Outline: Search validation from X page to Y page
    Given Navigate to "ebay.com"
    And In search bar type "<product_name>"
    And Click the "Search" button
    Then our items "<product_name>" are related on pages from "<start_page_number>" to "<finish_page_number>"

    Examples:
      | product_name | start_page_number | finish_page_number |
      | dress        | 12            |   13          |
      | iphone       | 13            |   14          |
      | samsung      | 9             |   6           |