import pytest
from pages.personal_account_page import PersonalAccountPage

@pytest.mark.usefixtures("setup")
class TestPersonalAccount:
    def test_open_account(self):
        account_page = PersonalAccountPage(self.driver)
        account_page.open_account()
        assert "account" in self.driver.current_url

    def test_open_order_history(self):
        account_page = PersonalAccountPage(self.driver)
        account_page.open_account()
        account_page.open_order_history()
        assert "order-history" in self.driver.current_url

    def test_logout(self):
        account_page = PersonalAccountPage(self.driver)
        account_page.open_account()
        account_page.logout()
        assert "login" in self.driver.current_url
