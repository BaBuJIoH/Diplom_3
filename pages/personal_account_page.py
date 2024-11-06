from locators.locators import PersonalAccountPageLocators
from pages.base_page import BasePage
import allure

class PersonalAccountPage(BasePage):
    @allure.step("Открыть личный кабинет")
    def open_account(self):
        self.click(PersonalAccountPageLocators.ACCOUNT_BUTTON)

    @allure.step("Перейти в историю заказов")
    def open_order_history(self):
        self.click(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click(PersonalAccountPageLocators.LOGOUT_BUTTON)
