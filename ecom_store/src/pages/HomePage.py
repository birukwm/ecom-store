
from ecom_store.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ecom_store.src.configs.MainConfigs import MainConfigs
from ecom_store.src.pages.locators.HomePageLocators import HomePageLocators





class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = MainConfigs.get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)

    def get_all_product_elements(self):
        return self.sl.wait_and_get_elements(self.PRODUCT)

    def get_displayed_heading(self):
        return self.sl.wait_and_get_text(self.PAGE_HEADING)

    def select_sort_by_price(self):

        self.sl.wait_and_select_dropdown(self.SORT,'Sort by price: low to high')
    def verify_the_product_are_listed_by_ascending_price(self):

        product_prices = self.sl.wait_and_get_elements(self.PRODUCT_AMOUNT)
        my_list = [price.text for price in product_prices]
        # remove the $ sign from the price list and convert them to float
        new_list = [float(i[1:]) for i in my_list]
        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i+1]:
                raise Exception(" Order by price ")


