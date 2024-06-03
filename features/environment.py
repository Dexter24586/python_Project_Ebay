import os

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.username = 'Test User'
    context.password = os.environ['SECRET']
def before_feature(context, feature):
    context.url = "https://www.ebay.com"
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
def before_step(context, step):
    ...
def after_step(context, step):
    if step.status == 'failed':
        current_dir = os.path.dirname(__file__)  # where this file located
        relative_path_to_dest = os.path.abspath(os.path.join(current_dir, 'failed_screenshots'))

        context.driver.save_screenshot(os.path.join(relative_path_to_dest, f'{step.name}.png'))
def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()
def after_feature(context, feature):
    ...
def after_all(context):
    ...