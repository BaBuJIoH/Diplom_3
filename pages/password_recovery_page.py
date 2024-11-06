from locators.locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
import allure

class PasswordRecoveryPage(BasePage):
    @allure.step("Кликнуть на кнопку 'Восстановить пароль'")
    def click_recovery_button(self):
        self.click(PasswordRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step("Ввести почту {email}")
    def enter_email(self, email):
        self.enter_text(PasswordRecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step("Отправить форму восстановления")
    def submit_recovery(self):
        self.click(PasswordRecoveryPageLocators.SUBMIT_BUTTON)

    @allure.step("Переключить видимость пароля")
    def toggle_password_visibility(self):
        self.click(PasswordRecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверить, что поле пароля подсвечено")
    def is_password_field_highlighted(self):
        return self.is_element_visible(PasswordRecoveryPageLocators.EMAIL_INPUT)
