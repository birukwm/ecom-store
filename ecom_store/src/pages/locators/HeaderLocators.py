

from selenium.webdriver.common.by import By

class HeaderLocators:

    CART_RIGHT_HEADER = (By.ID, 'site-header-cart')
    CART_ITEM_COUNT = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')
    MENU_ITEMS = (By.CSS_SELECTOR, 'div.menu ul.nav-menu li')
    SEARCH_FIELD = (By.ID, 'woocommerce-product-search-field-0')
    PRODUCTS = (By.CSS_SELECTOR, 'h1.product_title')
