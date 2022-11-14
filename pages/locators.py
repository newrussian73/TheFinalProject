from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    MESSAGE_ADD_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    NAME_OF_GOOD = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    COST_OF_BOOK = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    MESSAGE_COST_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
