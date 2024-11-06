import pytest
import allure
from pages.personal_account_page import PersonalAccountPage

@pytest.mark.usefixtures("setup")
class TestPersonalAccount:

    @allure.title("Проверка перехода по клику на 'Личный кабинет'")
    def test_navigate_to_personal_account(self):
        personal_account_page = PersonalAccountPage(self.driver)
        personal_account_page.open_account()
        assert "account" in self.driver.current_url

    @allure.title("Проверка перехода в раздел 'История заказов'")
    def test_navigate_to_order_history(self):
        personal_account_page = PersonalAccountPage(self.driver)
        personal_account_page.open_order_history()
        assert "order-history" in self.driver.current_url

    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self):
        personal_account_page = PersonalAccountPage(self.driver)
        personal_account_page.logout()
        assert "login" in self.driver.current_url
