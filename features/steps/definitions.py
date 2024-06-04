from selenium.webdriver.support import expected_conditions as EC
from behave import step
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


@step('Navigate to eBay.com')
def step_impl(context):
    # context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get(context.url)


@step('In search bar type "{input_var}"')
def step_impl(context, input_var):
    # searchbar = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(By.XPATH, "//input[@type='text']"))
    searchbar = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")), message= "Can't find the search bar")
    searchbar.send_keys(f"{input_var}")


@step('Click the "Search" button')
def step_impl(context):
    # s_button = context.driver.find_element(By.XPATH, "//input[@type='submit']")
    s_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")), message="Can't find the search button")
    s_button.click()


@step("Click the first dress from the page")
def step_impl(context):
    # first_item = context.driver.find_element(By.XPATH, "(//div[@class='srp-items-carousel__items-container']//li[@class='carousel__snap-point srp-items-carousel__list-item'])[1]")
    first_item = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='srp-items-carousel__items-container']//li[@class='carousel__snap-point srp-items-carousel__list-item'])[1]")), message="Can't find the first item")
    first_item.click()


@step('Click the "Sign In" button')
def step_impl(context):
    # sign_in_button = context.driver.find_element(By.XPATH, "//span[@id = 'gh-ug']/a[text() = 'Sign in']")
    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//span[@id = 'gh-ug']/a[text() = 'Sign in']")), message="Can't find sign in button")
    sign_in_button.click()


@step('Verify that "Sign In" page is loaded')
def step_impl(context):
    #title_name = context.driver.find_element(By.XPATH, "//title[contains(text(),'Sign in or Register | eBay')]").get_attribute("textContent")
    title_name = context.driver.title
    expected_title = "Sign in or Register | eBay"
    if title_name == expected_title:
        print("Page is loaded")
    else: print("Page is not loaded")


@step('Click the "register" button')
def step_impl(context):
    # register_button = context.driver.find_element(By.XPATH, "//span[@id='gh-ug-flex']/a[text() = 'register']")
    register_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//span[@id='gh-ug-flex']/a[text() = 'register']")),
        message="Can't find register button")
    register_button.click()


@step('Verify that "register" page is loaded')
def step_impl(context):
    #title_name = context.driver.find_element(By.XPATH, "//title[contains(text(),'Register: Create a personal account')]").get_attribute("textContent")
    title_name = context.driver.title
    expected_title = "Register: Create a personal account"
    if title_name == expected_title:
        print("Page is loaded")
    else: print("Page is not loaded")


@step('Click "{var1}" button')
def step_impl(context, var1):
    # daily_deals_button = context.driver.find_element(By.XPATH, f"//*[contains(@class, 'gh-') and normalize-space(text()) = '{var1}']")
    top_menu_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        f"//*[contains(@class, 'gh-') and normalize-space(text()) = '{var1}']")),
        message="Can't find top menu button")
    top_menu_button.click()


@step('Verify that "{page_title}" page is loaded with title')
def step_impl(context, page_title):
    # title_name = context.driver.find_element(By.XPATH, f"//title[contains(text(), '{page_title}')]")
    title_name = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        f"//title[contains(text(), '{page_title}')]")),
        message=f"Title is not equal to {page_title}")
    expected_title = "Daily Deals on eBay | Best deals and Free Shipping"
    if title_name == expected_title:
        print("Page is loaded")
    else:
        print("Page is not loaded")


@step('Click the "Watchlist" button')
def step_impl(context):
    # watchlist_button = context.driver.find_element(By.XPATH, "//a[@class= 'gh-eb-li-a gh-rvi-menu watchlist-menu'][text() = 'Watchlist']")
    watchlist_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//a[@class= 'gh-eb-li-a gh-rvi-menu watchlist-menu'][text() = 'Watchlist']")),
        message="Can't find watchlist button")
    watchlist_button.click()


@step('Verify that "Sign In Watchlist" button is displayed')
def step_impl(context):
    try:
        # sign_in_watchlist_button = context.driver.find_element(By.XPATH, "//div[@class='rvi__title']/a[text()='sign in']")
        sign_in_watchlist_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@class='rvi__title']/a[text()='sign in']")),
            message="Can't find sign in watchlist button")
        print("Sign In button is present.")
    except NoSuchElementException:
        print("Sign In button is not present.")
        sign_in_watchlist_button = None

    assert sign_in_watchlist_button is not None, "Sign In button should be present on the page."


@step('Click the "My eBay" button')
def step_impl(context):
    # my_ebay_button = context.driver.find_element(By.XPATH, "//a[@class= 'gh-eb-li-a gh-rvi-menu' and text() = 'My eBay']")
    my_ebay_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//a[@class= 'gh-eb-li-a gh-rvi-menu' and text() = 'My eBay']")),
        message="Can't find My eBay button")
    my_ebay_button.click()


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
    # my_ebay_button = context.driver.find_element(By.XPATH, "//a[@class= 'gh-eb-li-a gh-rvi-menu' and text() = 'My eBay']")
    my_ebay_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//a[@class= 'gh-eb-li-a gh-rvi-menu' and text() = 'My eBay']")),
        message="Can't find My eBay button")
    actions = ActionChains(context.driver)
    actions.move_to_element(my_ebay_button).perform()


@step('Verify that "My eBay" drop down list is displayed')
def step_impl(context):
    try:
        # drop_down_list = context.driver.find_element(By.XPATH, "//ul[@id='gh-ul-nav']")
        drop_down_list = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//ul[@id='gh-ul-nav']")),
            message="Can't find drop down list button")
        print("List is present")
    except NoSuchElementException:
        print("List is not present.")
        drop_down_list = None

    assert drop_down_list is not None, "List should be present on the page."


@step('Hover over "Alert" button')
def step_impl(context):
    # alert_button = context.driver.find_element(By.XPATH, "//i[@class= 'gh-sprRetina' and text() = 'Notification']")
    alert_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//i[@class= 'gh-sprRetina' and text() = 'Notification']")),
        message="Can't find alert button")
    actions = ActionChains(context.driver)
    actions.move_to_element(alert_button).perform()


@step('Verify that "Sign In Alert" button is displayed')
def step_impl(context):
    try:
        # sign_in_alert_button = context.driver.find_element(By.XPATH, "//div[@id='ghn-err']//span[text()='sign-in']")
        sign_in_alert_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[@id='ghn-err']//span[text()='sign-in']")),
            message="Can't find sign in alert button")
        assert sign_in_alert_button.is_displayed(), "'Sign In Alert' button is displayed"
        print("'Sign In Alert' button is displayed")
    except NoSuchElementException:
        assert False, "'Sign In Alert' button is displayed"
    except AssertionError as error:
        print(error)


@step('Click the "Cart" button')
def step_impl(context):
    # cart_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Your shopping cart']")
    cart_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//a[@aria-label='Your shopping cart']")),
        message="Can't find sign in cart button")
    cart_button.click()



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
    # cart_button = context.driver.find_element(By.XPATH, "//a[@aria-label='Your shopping cart']")
    cart_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//a[@aria-label='Your shopping cart']")),
        message="Can't find sign in cart button")
    actions = ActionChains(context.driver)
    actions.move_to_element(cart_button).perform()


@step('Verify that "Your cart is empty" pop up message is displayed')
def step_impl(context):
    try:
        # empty_cart_text = context.driver.find_element(By.XPATH, "//h2[@class='gh-minicart-header__title ']")
        empty_cart_text = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//h2[@class='gh-minicart-header__title ']")),
            message="Can't find empty cart TEXT")
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

    # add_to_cart_button = context.driver.find_element(By.XPATH, "//span[@class='ux-call-to-action__text'][text()='Add to cart']")
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//span[@class='ux-call-to-action__text'][text()='Add to cart']")),
        message="Can't find add to cart button")
    add_to_cart_button.click()

@step('Style filter "{filter_name}" by "{value}"')
def filter_by_value(context, filter_name, value):
    expand_button = context.driver.find_element(By.XPATH, f"//div[text()='{filter_name}']")
    if filter_name.lower() == "Style" or "Pattern" or "Season" or "Theme":
       expand_button.click()
       # filter_option = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[text()='{filter_name}']]//div[@class='x-refine__select__svg'][.//span[text()='{value}']]//input")
       filter_option = WebDriverWait(context.driver, 10).until(
           EC.presence_of_element_located((By.XPATH,
                                           f"//li[@class='x-refine__main__list '][.//div[text()='{filter_name}']]//div[@class='x-refine__select__svg'][.//span[text()='{value}']]//input")),
           message="Can't find filter option")
       filter_option.click()
       sleep(3)

    else:
        filter_option = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"//li[@class='x-refine__main__list '][.//div[text()='{filter_name}']]//div[@class='x-refine__select__svg'][.//span[text()='{value}']]//input")),
            message="Can't find filter option")
        filter_option.click()




@step('Size filter "{size_name}" for "{size_type}" and "{value}"')
def filter_by_size(context, size_name:str, size_type, value):
    if size_name.lower() == "Regular".lower():
        # filter_option = context.driver.find_element(By.XPATH, f"'//li[@class='x-refine__main__list '][.//div[text()='Size']]//div[@class='size-component__container']//span[text()='{size_type}']/following-sibling::span[text()='{value}]")
        filter_option = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"'//li[@class='x-refine__main__list '][.//div[text()='Size']]//div[@class='size-component__container']//span[text()='{size_type}']/following-sibling::span[text()='{value}]")),
            message="Can't find filter option")
        filter_option.click()
        sleep(3)
    else:
        # button = context.driver.find_element(By.XPATH, f"//h4[contains(text(),'{size_name}')]")
        button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"//h4[contains(text(),'{size_name}')]")),
            message="Can't find size option")
        button.click()
        # filter_option = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[text()='Size']]//div[@class='size-component__container']//span[text()='{size_type}']/following-sibling::span[text()='{value}']" )
        filter_option = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"//li[@class='x-refine__main__list '][.//div[text()='Size']]//div[@class='size-component__container']//span[text()='{size_type}']/following-sibling::span[text()='{value}']")),
            message="Can't find size filter option option")
        filter_option.click()

@step('Choose "{color_value}" color')
def filter_color(context, color_value):
    # color_button = context.driver.find_element(By.XPATH, f"//span[text()='{color_value}']")
    color_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        f"//span[text()='{color_value}']")),
        message="Can't find color button")
    color_button.click()
@step('in "{option1}" click "{option2}"')
def step_impl(context, option1, option2):
    # radio_button = context.driver.find_element(By.XPATH, f"//li[@class='x-refine__main__list '][.//div[text()='{option1}']]//span[text()='{option2}']/../..//input[@type='radio']")
    radio_button = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        f"//li[@class='x-refine__main__list '][.//div[text()='{option1}']]//span[text()='{option2}']/../..//input[@type='radio']")),
        message="Can't find radio button")
    radio_button.click()


@step('all items are "{desired_title}" related')
def check_all_items_titles(context, desired_title):
    # all_items = context.driver.find_elements(By.XPATH, "//li[contains(@id, 'item')]//span[@role='heading']")
    all_items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//li[contains(@id, 'item')]//span[@role='heading']")),
        message="Can't find all items titles")
    issues = []

    for item in all_items:
        title = item.text
        if desired_title.lower() not in title.lower():
            issues.append(f'{title} is not {desired_title} related')

    if issues:
        raise Exception(f'Following issues discovered: {issues}')

@step('validate tha all dresses "{key_name}" are "{expected_value}"')
def validate_detailed_filtering(context, key_name, expected_value):
    all_items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//li[contains(@id, 'item')]")),
        message="Can't find all items titles")
    main_window = context.driver.current_window_handle
    issues = []

    for item in all_items:
        title = item.find_element((By.XPATH, ".//span[@role='heading']"))
        product_url = item.find_element((By.XPATH,))
        # get to the item page

        # click
        # switch
        # collect item specs

        # do the validation
        # close
        context.driver.close()
        # switch
        context.driver.switch_to.window(main_window)

    if issues:
        raise Exception(f'Following issues discovered: {issues}')





@step('all items are "{our_search2}" related on "{page_quantity1}" amount of pages')
def step_impl(context, our_search2, page_quantity1):
    page_quantity = int(page_quantity1)
    issues = []
    for page_number in range(1, page_quantity+1):
        all_items = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//li[contains(@id, 'item')]//span[@role='heading']")),
            message="Can't find all items titles")

        for item in all_items:
            title = item.text
            if our_search2.lower() not in title.lower():
               issues.append(f'{title} is not {our_search2} related')

        # page_button = context.driver.find_element(By.XPATH, f"//a[text()='{page_number + 1}']")
        page_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            f"//a[text()='{page_number + 1}']")),
            message="Can't find page button")
        page_button.click()

    if issues:
        raise Exception(f'Following issues discovered: {issues}')


# @step('our items "{product_name}" are related on pages from "{start_page_number}" to "{finish_page_number}"')
# def step_impl(context, product_name, start_page_number, finish_page_number):
#     issues = []
#
#     start_page_number, finish_page_number = int(start_page_number), int(finish_page_number)
#
#     def check_items():
#         all_items = WebDriverWait(context.driver, 10).until(
#             EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@id, 'item')]//span[@role='heading']"))
#         )
#
#         for item in all_items:
#             title = item.text
#             if product_name.lower() not in title.lower():
#                 issues.append(f'{title} is not {product_name} related')
#
#     if start_page_number <= finish_page_number:
#         for page_number in range(start_page_number, finish_page_number + 1):
#             page_button = WebDriverWait(context.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, f"//a[text()='{page_number}']")))
#             page_button.click()
#             sleep(2)
#             check_items()
#     else:
#         for page_number in range(start_page_number, finish_page_number - 1, -1):
#             page_button = WebDriverWait(context.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, f"//a[text()='{page_number}']")))
#             page_button.click()
#             sleep(2)
#             check_items()
#
#     if issues:
#         raise Exception(f'Following issues discovered: {issues}')
@step('our items "{product_name}" are related on pages from "{start_page_number}" to "{finish_page_number}"')
def step_impl(context, product_name, start_page_number, finish_page_number):
    issues = []
    start_page_number, finish_page_number = int(start_page_number), int(finish_page_number)
    def check_items():
        all_items = WebDriverWait(context.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@id, 'item')]//span[@role='heading']")), message="Can't find page button")
        for item in all_items:
            title = item.text
            if product_name.lower() not in title.lower():
                issues.append(f'{title} is not {product_name} related')

    def go_to_page(page_number):
        while True:
            try:
                # page_button = context.driver.find_element(By.XPATH, f"//a[text()='{page_number}']")
                page_button = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.XPATH, f"//a[text()='{page_number}']")),
                    message="Can't find page button")
                page_button.click()
                return True
            except:
                try:
                    next_page_button = WebDriverWait(context.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Go to next search page']")),
                    message="Can't find next page button")
                    next_page_button.click()
                except:
                    print(f"Page {page_number} does not exist and no more pages available.")
                    return False

    # Переход к стартовой странице
    if not go_to_page(start_page_number):
        raise Exception(f'Start page {start_page_number} does not exist.')

    if start_page_number <= finish_page_number:
        for page_number in range(start_page_number, finish_page_number + 1):
            check_items()
            if not go_to_page(page_number + 1):
                break
    else:
        for page_number in range(start_page_number, finish_page_number - 1, -1):
            check_items()
            if not go_to_page(page_number - 1):
                break

    if issues:
        raise Exception(f'Following issues discovered: {issues}')


@step('I click "Shop by category" button')
def step_impl(context):
    try:
        shop_by_cat_button = WebDriverWait(context.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@id='gh-shop-a']")),
                    message="Can't find shop by category button")
        shop_by_cat_button.click()

    except Exception as e: print(f"Exception occurred: {e}")


@step('menu "Shop by category" is displayed')
def step_impl(context):
    try:
        shop_by_category_menu = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='gh-sbc-o']")),
            message="Can't find shop by category button")
        assert shop_by_category_menu.is_displayed(), "Menu 'Shop by category' is not displayed"
    except Exception as e:
        raise AssertionError(f"An error occurred: {e}")


@step('"{category}" contains it\'s "{subcategories}"')
def step_impl(context, category, subcategories):
    issues = []

    expected_subcategories = [subcategory.strip() for subcategory in subcategories.split(';')]
    category_xpath = f"//h3/a[text() = '{category}']"
    category_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, category_xpath)),
                    message="Can't find category element")

    subcategory_xpath = f"//h3[a[text()='{category}']]/following-sibling::ul[1]//a"
    # subcategory_elements = category_element.find_elements(By.XPATH, subcategory_xpath)
    subcategory_elements = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, subcategory_xpath)),
        message="Can't find category element")
    actual_subcategories = [elem.text.strip() for elem in subcategory_elements]

    for expected_subcategory in expected_subcategories:
        if expected_subcategory not in actual_subcategories:
            issues.append(f'Subcategory "{expected_subcategory}" not found under category "{category}"')

    assert len(issues) == 0, f'Issues found:\n' + '\n'.join(issues)


@step("verify that slides are switching")
def carousel_slides_default(context):
    carousel_slides = WebDriverWait(context.driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'carousel__autoplay')]//ul/li"))
    )
    print(f'There are {len(carousel_slides)} slides in carousel')

    wait_for_element = WebDriverWait(context.driver, 4 * len(carousel_slides))

    for slide in carousel_slides:

        wait_for_element.until(EC.visibility_of(slide), message=f'Slide {carousel_slides.index(slide)} was not visible')

        wait_for_element.until(EC.invisibility_of_element(slide), message=f'Slide {carousel_slides.index(slide)} remained visible')

        print(f'Slide {carousel_slides.index(slide)} is fine')

@step("verify that slider is active")
def step_impl(context):
    try:
        play_pause_button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Pause Banner Carousel']"))
        )
        print("Slider is active as expected")
    except TimeoutException:
        raise AssertionError("Slider is not active")

@step('I click on {play_or_pause_button} button')
def step_impl(context, play_or_pause_button):
    try:
        button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//button[@aria-label='{play_or_pause_button} Banner Carousel']"))
        )
        button.click()
    except TimeoutException:
        raise AssertionError(f"{play_or_pause_button} button is not active")

@step("verify that slider is paused")
def step_impl(context):
    try:
        button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Play Banner Carousel']"))
        )
        print("Slider is paused as expected")
    except TimeoutException:
        raise AssertionError("Slider is not paused")

@step("verify that slide is changed to the next one")
def step_impl(context):
    try:
        next_slide_dot = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class ='vl-carousel--dots']/ul/li[2][@class='vl-carousel--dots__active']"))
        )
        print("Slide is changed to the next one as expected")
    except TimeoutException:
        raise AssertionError("Slide did not change to the next one")

@step("verify that slide is changed to the previous one")
def step_impl(context):
    try:
        previous_slide_dot = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class ='vl-carousel--dots']/ul/li[1][@class='vl-carousel--dots__active']"))
        )
        print("Slide is changed to the previous one as expected")
    except TimeoutException:
        raise AssertionError("Slide did not change to the previous one")


@step("I click on {next_previous_button} button.")
def step_impl(context, next_previous_button):
    try:
        button = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//button[@aria-label='{next_previous_button}']")))
        button.click()
    except TimeoutException:
        raise AssertionError(f"{next_previous_button} button is not active")
