import pytest
from ecom_store.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_negative(self):

        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('nonexistinguser')
        my_account.input_login_password('nonexistingpassword')
        my_account.click_register_button()
        expected_err = 'Error: Please provide a valid email address.'
        my_account.wait_until_error_is_displayed(expected_err)


