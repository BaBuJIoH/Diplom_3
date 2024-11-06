import pytest
import allure
from pages.password_recovery_page import PasswordRecoveryPage
from locators.locators import PasswordRecoveryPageLocators

@pytest.mark.usefixtures("setup")
class TestPasswordRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_navigate_to_recovery_page(self):
        recovery_page = PasswordRecoveryPage(self.driver)
        recovery_page.click_recovery_button()
        assert "password-recovery" in self.driver.current_url

    @allure.title("Проверка восстановления пароля с вводом почты")
    def test_recover_password(self):
        recovery_page = PasswordRecoveryPage(self.driver)
        recovery_page.enter_email("user@example.com")
        recovery_page.submit_recovery()
        assert recovery_page.is_element_visible(PasswordRecoveryPageLocators.RECOVERY_CONFIRMATION)

    @allure.title("Проверка переключения видимости поля пароля")
    def test_toggle_password_visibility(self):
        recovery_page = PasswordRecoveryPage(self.driver)
        recovery_page.toggle_password_visibility()
        assert recovery_page.is_password_field_highlighted()
