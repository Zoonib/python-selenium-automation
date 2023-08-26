from behave import given, when, then
from selenium.webdriver.common.by import By

from behave import given, when, then
from selenium.webdriver.common.by import By

def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@given('Open amazon')


@when('Click on Best Seller')
def click_best_Seller(context):
    context.driver.find_element(By.CSS_SELECTOR, '#zg_header a').click()


@then('Verify header has {expected_number}links')
def verify_un_order_list(context, expected_number):
    expected_amount = int(expected_number)
    links = context.driver.find_elements(*Header_Link)
    assert len(links) == expected_number, f'Expected {expected_number}links but got {len(links)}'













