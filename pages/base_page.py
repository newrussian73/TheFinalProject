import math

import allure
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage():
    """
    Основной класс с методами для всего проекта
    """
    # Инициализация браузера
    def __init__(self, browser, url, timeout=10):
        with allure.step(f"Открытие браузера{browser}"):
            self.browser = browser
            self.url = url
            self.browser.implicitly_wait(timeout)

    # Открытие сайта (url)
    def open(self):
        with allure.step(f"Открытие ссылки {self.url}"):
            self.browser.get(self.url)

    # Сообщение если попадает исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Для решение уравнения для Stepik.org
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Проверка, что элемент не присутствует на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # Ожидания исчезания элемента со страницы
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Переход на страницу логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    # наличие веб-элемента (кнопки) для перехода на страницу логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Переход на страницу корзины
    def go_to_basket(self):
        button_basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        button_basket.click()

    # Проверка, что пользователь авторизован
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
