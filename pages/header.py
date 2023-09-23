from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    NAV_ORDERS = (By.ID, 'nav-orders')
    DEPT_SELECTION = (By.ID, 'searchDropdownBox')
    SUBHEADER_DEPT = (By.XPATH, "//option[@selected='selected' and @value='search-alias=mobile']")

    def click_signin_popup(self, *locator):
        self.click(*self.NAV_ORDERS)

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def select_dept(self):
        dept_selection = self.find_element(*self.DEPT_SELECTION)
        select = Select(dept_selection)
        select.select_by_value('search-alias=mobile')

    def search_iphone(self, text):
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def verify_dept_selected(self):
        self.wait_for_element_appear(*self.SUBHEADER_DEPT)