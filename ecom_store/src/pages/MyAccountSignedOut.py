
from ecom_store.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from ecom_store.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ecom_store.src.configs.MainConfigs import MainConfigs
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocators):

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
    def click_lost_your_password_link(self):
        self.sl.wait_and_click(self.LOST_PASSWORD)
    def input_lost_password_email(self, email='birbisrat@gmail.com'):

        self.sl.wait_and_input_text(self.LOST_PASS_USER, email)
    def click_reset_password_button(self):
        self.sl.wait_and_click(self.RESET_PASSWORD)
    def verify_correct_password_reset_message_is_displayed(self):

        my_alert = self.sl.wait_until_element_is_visible(self.Message_ALERT)
        actual_message = my_alert.text
        expected_message = 'Password reset email has been sent.'

        assert actual_message == expected_message ,f" Correct alert message is not displayed, \
            instead {actual_message} is printed "


