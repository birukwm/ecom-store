import os

import pytest

from ecom_store.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")

class TestLoginPositive:
    @pytest.mark.tcidb2
    def test_login_positive(self):

        my_account = MyAccountSignedOut(self.driver)

        # go to my accountsignedout page
        my_account.go_to_my_account()

        # fill in username and password
        user = os.environ['USER']
        passwordlp = os.environ['PASSWORDLP']
        my_account.input_login_username(user)
        my_account.input_login_password(passwordlp)
        my_account.click_login_button()
        my_account.verify_user_is_logged_in()



