import pytest
from ecom_store.src.pages.HomePage import HomePage
@pytest.mark.usefixtures("init_driver")

class TestSortingByPrice:
    @pytest.mark.tcid055
    def test_sort_products_by_price(self):

        my_homepage = HomePage(self.driver)

        my_homepage.go_to_home_page()
        my_homepage.select_sort_by_price()
        my_homepage.verify_the_product_are_listed_by_ascending_price()


        #go to homepage
        #select sorting by price
        #make sure products are sorted by price
