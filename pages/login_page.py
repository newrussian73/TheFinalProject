import faker

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка на присутствие слова login в текущей ссылке
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "don't consist word 'login' in url"

    # Проверка на наличия формы авторизации на странице логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Not exist form of login in login page"

    # Проверка на наличия формы регистрации на странице логина
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "not exist form of register in login page"

    # Создание нового пользователя
    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = f.password() + "123"
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.R_PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()