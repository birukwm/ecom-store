import pytest
from ecom_store.src.pages.MyAccountSignedOut import MyAccountSignedOut
@pytest.mark.usefixtures("init_driver")

class TestPasswordResetLinkIsFunctional:

    @pytest.mark.tcid045
    def test_password_rest_link_Is_functional(self):

        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.click_lost_your_password_link()
        my_account.input_lost_password_email()
        my_account.click_reset_password_button()
        my_account.verify_correct_password_reset_message_is_displayed()





