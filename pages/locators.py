from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    MESSAGE_ADD_BASKET = (By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-success.fade.in')
    NAME_OF_GOOD = (By.CLASS_NAME, 'col-sm-6.product_main')
    COST_OF_BOOK = (By.CLASS_NAME, 'price_color')
    MESSAGE_COST_BASKET = (By.CLASS_NAME, 'alert.alert-safe.alert-noicon.alert-info.fade.in')
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
