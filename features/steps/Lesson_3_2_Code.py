from behave import given, when, then
from selenium.webdriver.common.by import By

from behave import given, when, then
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.by import By

from behave import given, when, then
from selenium.webdriver.common.by import By



@given('Open amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Click on Orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()



@then('Verify Sign in page opened')
def verify_signin_page_opened(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-box-inner .a-spacing-small').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
