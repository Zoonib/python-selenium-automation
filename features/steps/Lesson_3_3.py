from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Click on Cart')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()



@then('Verify cart is empty')
def verify_cart_empty(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'