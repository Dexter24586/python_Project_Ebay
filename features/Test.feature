Feature: Ebay Regression

  Background: Generic navigation
    Given Navigate to eBay.com

 Scenario: Search bar Verification
    And In search bar type "dress"
    And Click the "Search" button
    Then Click the first dress from the page
    And click add to cart
    #Then click "go to cart"
    #And Item was added to the cart


 Scenario: "Sign in" page is loading verification
    And Click the "Sign In" button
    Then Verify that "Sign In" page is loaded

 Scenario: "register" page is loading verification
    And Click the "register" button
    Then Verify that "register" page is loaded

  Scenario Outline: page loading verification
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
    And Click the "Watchlist" button
    Then Verify that "Sign In Watchlist" button is displayed

  Scenario: "My eBay" page is loading verification
    And Click the "My eBay" button
    Then Verify that "My eBay" page is loaded

  Scenario: "My eBay" drop down list is displayed
    And Hover over "My eBay" button
    Then Verify that "My eBay" drop down list is displayed

  Scenario: After hover over on "Alert" button "Sign In" button is displayed
    And Hover over "Alert" button
    Then Verify that "Sign In Alert" button is displayed

  Scenario: "Cart" page is loading verification
    And Click the "Cart" button
    Then Verify that "Cart" page is loaded

  Scenario: After hover over on "Cart" button "Your cart is empty" pop up message is displayed
    And Hover over "Cart" button
    Then Verify that "Your cart is empty" pop up message is displayed

  Scenario: Filter validation for style
    And In search bar type "dress"
    And Click the "Search" button
    Then Style filter "Pattern" by "Solid"

  Scenario: Filter validation for size
    And In search bar type "dress"
    And Click the "Search" button
    Then Size filter "Junior" for "Juniors Size" and "XS"

  Scenario: Filter validation for Color
    And In search bar type "dress"
    And Click the "Search" button
    Then Choose "Black" color

  Scenario: Filter validation for Buying format or Item Location
    And In search bar type "dress"
    And Click the "Search" button
    Then in "Item Location" click "US Only"

  Scenario Outline: Search validation
    And In search bar type "<our_search1>"
    Then all items are "<our_search1>" related

    Examples:
      | our_search1 |
      | dress       |
      | iphone      |
      | samsung     |

  Scenario Outline: Search validation on X pages
    And In search bar type "<our_search2>"
    And Click the "Search" button
    Then all items are "<our_search2>" related on "<page_quantity1>" amount of pages

    Examples:
      | our_search2 | page_quantity1 |
      | dress       | 2              |
      | iphone      | 3              |
      | samsung     | 3              |


  Scenario Outline: Search validation from X page to Y page
    And In search bar type "<product_name>"
    And Click the "Search" button
    Then our items "<product_name>" are related on pages from "<start_page_number>" to "<finish_page_number>"

    Examples:
      | product_name | start_page_number | finish_page_number |
      | dress        | 1            |   99999999999999999999999999          |
      | iphone       | 13            |   14          |
      | samsung      | 9             |   6           |


  Scenario Outline: Validate Shop By category menu
    And I click "Shop by category" button
    And menu "Shop by category" is displayed
    Then "<category>" contains it's "<subcategories>"

    Examples:
      | category | subcategories |
      | Motors | Parts & accessories; Cars & trucks; Motorcycles; Other vehicles |
      | Clothing & Accessories | Women; Men; Handbags; Collectible Sneakers |
      | Sporting goods | Hunting Equipment; Golf Equipment; Outdoor sports; Cycling Equipment |
      | Electronics | Computers, Tablets & Network Hardware; Cell Phones, Smart Watches & Accessories; Video Games & Consoles; Cameras & Photo |
      | Business & Industrial | Modular & Pre-Fabricated Buildings; Test, Measurement & Inspection Equipment; Heavy Equipment, Parts & Attachments; Restaurant & Food Service |
      | Jewelry & Watches | Luxury Watches; Wristwatches; Fashion Jewelry; Fine Jewelry |
      | Collectibles & Art | Trading Cards; Collectibles; Coins & Paper Money; Sports Memorabilia |
      | Home & garden | Yard, Garden & Outdoor Living Items; Tools & Workshop Equipment; Home Improvement; Kitchen, Dining & Bar Supplies |
      | Other categories | Books, Movies & Music; Toys & Hobbies; Health & Beauty; Baby Essentials |

  Scenario: Validate slide banner
    And verify that slides are switching
    And verify that slider is active
    And I click on Pause button
    And verify that slider is paused
    And I click on Go to next banner button.
    And verify that slide is changed to the next one
    And I click on Go to previous banner button.
    And verify that slide is changed to the previous one


  Scenario: Filter validation - length
    And In search bar type "dress"
    And Click the "Search" button
    Then Style filter "Dress Length" by "Short"
    Then validate tha all dresses "Dress Length" are "Short"