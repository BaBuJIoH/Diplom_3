import pytest
from pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestMainFunctionality:
    def test_navigate_to_constructor(self):
        main_page = MainPage(self.driver)
        main_page.click_constructor_button()
        assert "constructor" in self.driver.current_url

    def test_navigate_to_order_feed(self):
        main_page = MainPage(self.driver)
        main_page.click_order_feed_button()
        assert "order-feed" in self.driver.current_url

    def test_view_ingredient_details(self):
        main_page = MainPage(self.driver)
        main_page.click_ingredient_button()
        assert main_page.is_ingredient_details_popup_displayed()

    def test_close_ingredient_details_popup(self):
        main_page = MainPage(self.driver)
        main_page.click_ingredient_button()
        main_page.close_ingredient_details_popup()
        assert not main_page.is_ingredient_details_popup_displayed()

    def test_add_ingredient_to_order_increases_counter(self):
        main_page = MainPage(self.driver)
        initial_count = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        assert main_page.get_ingredient_counter() == initial_count + 1

    def test_logged_in_user_can_place_order(self):
        main_page = MainPage(self.driver)
        main_page.login_user()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        assert main_page.is_order_confirmation_displayed()
