import pytest
from ecom_store.src.pages.HomePage import HomePage
from ecom_store.src.pages.Header import Header
@pytest.mark.usefixtures("init_driver")
class TestProductSearchGivesRightProduct:
    @pytest.mark.tcid03
    def test_product_search_gives_related_items(self):
        my_homepage = HomePage(self.driver)
        #go to home page
        my_homepage.go_to_home_page()
        #search a product
        my_header = Header(self.driver)
        my_header.search_random_existing_product()
        my_header.search_product_with_return_key()
        my_header.verify_searched_item_is_displayed()
        # verify the searched item is displayed on the serch result