
from selenium.webdriver.common.by import By

class HomePageLocators:

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'a.add_to_cart_button')
    PRODUCT = (By.CSS_SELECTOR, 'ul.products li.product')

    PAGE_HEADING = (By.CSS_SELECTOR, 'header.woocommerce-products-header h1.page-title')

    SORT = (By.XPATH, '/html/body/div/div/div/div[2]/main/div[1]/form/select')

    PRODUCT_AMOUNT = (By.CSS_SELECTOR, 'span.woocommerce-Price-amount.amount')