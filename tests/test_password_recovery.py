import pytest
from pages.password_recovery_page import PasswordRecoveryPage

@pytest.mark.usefixtures("setup")
class TestPasswordRecovery:
    def test_navigate_to_recovery_page(self):
        recovery_page = PasswordRecoveryPage(self.driver)
        recovery_page.click_recovery_button()
        assert "password-recovery" in self.driver.current_url

    def test_recover_password(self):
        recovery_page = PasswordRecoveryPage(self.driver)
        recovery_page.enter_email("user@example.com")
        recovery_page.submit_recovery()
        # Проверить, что появляется уведомление об отправке письма

    def test_toggle_password_visibility(self):
        recovery_page = PasswordRecoveryPage(self.driver)
        recovery_page.toggle_password_visibility()
        # Проверить, что поле пароля подсвечивается
