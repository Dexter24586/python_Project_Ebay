from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@step("Navigate to ebay.com")
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("https://www.ebay.com/")


@step('In search bar type "dress"')
def step_impl(context):
    searchbar = context.driver.find_element(By.XPATH, "//input[@type='text']")
    searchbar.send_keys("dress")


@step('Click "Search" button')
def step_impl(context):
    s_button = context.driver.find_element(By.XPATH, "//input[@type='submit']")
    s_button.click()
    sleep(1)


@step("Click the first dress from the page")
def step_impl(context):
    first_item = context.driver.find_element(By.XPATH, "(//div[@class='srp-items-carousel__items-container']//li[@class='carousel__snap-point srp-items-carousel__list-item'])[1]")
    first_item.click()
    sleep(3)


@step('Click "Sign In" button')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.XPATH, "//span[@id = 'gh-ug']/a[text() = 'Sign in']")
    sign_in_button.click()
    sleep(1)


@step('Verify that "Sign In" page is loaded')
def step_impl(context):
    #title_name = context.driver.find_element(By.XPATH, "//title[contains(text(),'Sign in or Register | eBay')]").get_attribute("textContent")
    title_name = context.driver.title
    expected_title = "Sign in or Register | eBay"
    if title_name == expected_title:
        print("Page is loaded")
    else: print("Page is not loaded")


@step('Click "register" button')
def step_impl(context):
    register_button = context.driver.find_element(By.XPATH, "//span[@id='gh-ug-flex']/a[text() = 'register']")
    register_button.click()
    sleep(1)


@step('Verify that "register" page is loaded')
def step_impl(context):
    #title_name = context.driver.find_element(By.XPATH, "//title[contains(text(),'Register: Create a personal account')]").get_attribute("textContent")
    title_name = context.driver.title
    expected_title = "Register: Create a personal account"
    if title_name == expected_title:
        print("Page is loaded")
    else: print("Page is not loaded")


@step('Click "Daily Deals" button')
def step_impl(context):
    daily_deals_button = context.driver.find_element(By.XPATH, "//a[@class='gh-p' and text()=' Daily Deals']")
    daily_deals_button.click()
    sleep(1)


@step('Verify that "Daily Deals" page is loaded')
def step_impl(context):
    title_name = context.driver.title
    expected_title = "Daily Deals on eBay | Best deals and Free Shipping"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Click "Brand Outlet" button')
def step_impl(context):
    brand_outlet_button = context.driver.find_element(By.XPATH, "//a[@class='gh-p' and text()=' Brand Outlet']")
    brand_outlet_button.click()
    sleep(1)


@step('Verify that "Brand Outlet" page is loaded')
def step_impl(context):
    title_name = context.driver.title
    expected_title = "Brand Outlet products for sale | eBay"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Click "Gift Cards" button')
def step_impl(context):
    gift_cards_button = context.driver.find_element(By.XPATH, "//a[@class='gh-p' and text()=' Gift Cards']")
    gift_cards_button.click()
    sleep(1)


@step('Verify that "Gift Cards" page is loaded')
def step_impl(context):
    title_name = context.driver.title
    expected_title = "eBay Gift Cards | eBay.com"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Click "Help & Contact" button')
def step_impl(context):
    help_contact_button = context.driver.find_element(By.XPATH, "//a[@class='gh-p' and text()=' Help & Contact']")
    help_contact_button.click()
    sleep(1)


@step('Verify that "Help & Contact" page is loaded')
def step_impl(context):
    title_name = context.driver.title
    expected_title = "eBay Customer Service"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Click "Sell" button')
def step_impl(context):
    sell_button = context.driver.find_element(By.XPATH, "//a[@class='gh-p' and text()=' Sell']")
    sell_button.click()
    sleep(1)


@step('Verify that "Sell" page is loaded')
def step_impl(context):
    title_name = context.driver.title
    expected_title = "Selling on eBay | Electronics, Fashion, Home & Garden | eBay"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Click "Watchlist" button')
def step_impl(context):
    watchlist_button = context.driver.find_element(By.XPATH, "//a[@class= 'gh-eb-li-a gh-rvi-menu watchlist-menu'][text() = 'Watchlist']")
    watchlist_button.click()
    sleep(1)


@step('Verify that "Sign In Watchlist" button is displayed')
def step_impl(context):
    try:
        sign_in_watchlist_button = context.driver.find_element(By.XPATH, "//div[@class='rvi__title']/a[text()='sign in']")
        print("Sign In button is present.")
    except NoSuchElementException:
        print("Sign In button is not present.")
        sign_in_watchlist_button = None

    assert sign_in_watchlist_button is not None, "Sign In button should be present on the page."


@step('Click "My eBay" button')
def step_impl(context):
    my_ebay_button = context.driver.find_element(By.XPATH, "//a[@class= 'gh-eb-li-a gh-rvi-menu' and text() = 'My eBay']")
    my_ebay_button.click()
    sleep(1)


@step('Verify that "My eBay" page is loaded')
def step_impl(context):
    title_name = context.driver.title
    expected_title = "Security Measure"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Hover over "My eBay" button')
def step_impl(context):
    my_ebay_button = context.driver.find_element(By.XPATH, "//a[@class= 'gh-eb-li-a gh-rvi-menu' and text() = 'My eBay']")
    actions = ActionChains(context.driver)
    actions.move_to_element(my_ebay_button).perform()
    sleep(1)


@step('Verify that "My eBay" drop down list is displayed')
def step_impl(context):
    try:
        drop_down_list = context.driver.find_element(By.XPATH, "//ul[@id='gh-ul-nav']")
        print("List is present")
    except NoSuchElementException:
        print("List is not present.")
        drop_down_list = None

    assert drop_down_list is not None, "List should be present on the page."


@step('Hover over "Alert" button')
def step_impl(context):
    alert_button = context.driver.find_element(By.XPATH, "//i[@class= 'gh-sprRetina' and text() = 'Notification']")
    actions = ActionChains(context.driver)
    actions.move_to_element(alert_button).perform()
    sleep(1)


@step('Verify that "Sign In Alert" button is displayed')
def step_impl(context):
    try:
        sign_in_alert_button = context.driver.find_element(By.XPATH, "//div[@id='ghn-err']//span[text()='sign-in']")
        assert sign_in_alert_button.is_displayed(), "'Sign In Alert' button is displayed"
        print("'Sign In Alert' button is displayed")
    except NoSuchElementException:
        assert False, "'Sign In Alert' button is displayed"
    except AssertionError as error:
        print(error)


@step('Click "Cart" button')
def step_impl(context):
    cart_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Your shopping cart']")
    cart_button.click()
    sleep(1)


@step('Verify that "Cart" page is loaded')
def step_impl(context):
    title_name = context.driver.title
    expected_title = "eBay shopping cart"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Hover over "Cart" button')
def step_impl(context):
    cart_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Your shopping cart']")
    actions = ActionChains(context.driver)
    actions.move_to_element(cart_button).perform()
    sleep(1)


@step('Verify that "Your cart is empty" pop up message is displayed')
def step_impl(context):
    try:
        empty_cart_text = context.driver.find_element(By.XPATH, "//h2[@class='gh-minicart-header__title ']")
        assert empty_cart_text.is_displayed(), "'Your cart is empty' message should be visible."
        print("'Your cart is empty' message is displayed.")
    except NoSuchElementException:
        assert False, "'Your cart is empty' message is not displayed."
    except AssertionError as error:
        print(error)


@step("click add to cart")
def step_impl(context):
    context.current_window = context.driver.current_window_handle

    for window_handle in context.driver.window_handles:
        if window_handle != context.current_window:
             context.driver.switch_to.window(window_handle)
             break
    sleep(1)

    add_to_cart_button = context.driver.find_element(By.XPATH, "//span[@class='ux-call-to-action__text'][text()='Add to cart']")
    add_to_cart_button.click()
    sleep(1)

