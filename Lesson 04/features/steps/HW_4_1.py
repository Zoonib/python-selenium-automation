from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

Header_Link = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']") # Header_Link has been defined.

@given('Open Bestsellers')
def amazon_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(2)
    context.driver.refresh()

#3@when('Click on Best Seller')
#def click_best_Seller(context):
#    context.driver.find_element(By.CSS_SELECTOR, '[a.nav-a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]').click()

@then('Verify header has 5 links')
def verify_un_order_list(context):
   # expected_amount = int(expected_number)
    links = context.driver.find_elements(*Header_Link)
    assert len(links) == 5, f'Expected 5 links but got {len(links)}'













