from selenium.webdriver.common.by import By
from behave import *
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
#    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash', 'Indigo wash', 'light wash', 'Medium Blue Vintage' 'Medium Wash', 'Rinsed', 'Vitage Wash', 'Washed Black' , 'Bright white', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive' , 'Light Blue Vintage' , 'Washed Grey', 'Sage Green' '] # 0, 1, 2, 3, 4
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'