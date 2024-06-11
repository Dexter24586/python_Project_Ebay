import os
import re
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#

def before_all(context):
   ...
def before_feature(context, feature):
    context.url = "https://www.ebay.com"
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def before_step(context, step):
    ...
def after_step(context, step):
    if step.status == 'failed':
        current_dir = os.path.dirname(__file__)
        relative_path_to_dest = os.path.abspath(os.path.join(current_dir, 'failed_screenshots'))

        if not os.path.exists(relative_path_to_dest):
            os.makedirs(relative_path_to_dest)

        clean_name = '_'.join(re.findall(r"\w+", step.name))

        screenshot_path = os.path.join(relative_path_to_dest, f'{clean_name}.png')
        context.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()
def after_feature(context, feature):
    ...
def after_all(context):
    ...