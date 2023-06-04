
from ecom_store.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from ecom_store.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from ecom_store.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ecom_store.src.configs.MainConfigs import MainConfigs

import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocators, MyAccountSignedInLocators):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def go_to_my_account(self):
        base_url = MainConfigs.get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")

        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.debug("Clicking 'Register' button.")
        self.sl.wait_and_click(self.REGISTER_BTN)
    def verify_user_is_logged_in(self):
        logout_btn = self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)
        assert logout_btn.is_displayed() == True, f"valid user is not loged in "




