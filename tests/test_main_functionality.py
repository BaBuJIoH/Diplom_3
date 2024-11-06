import pytest
import allure
from pages.main_page import MainPage

@pytest.mark.usefixtures("setup")
class TestMainFunctionality:

    @allure.title("Проверка перехода по клику на кнопку 'Конструктор'")
    def test_click_constructor_button(self):
        main_page = MainPage(self.driver)
        main_page.click_constructor_button()
        assert "constructor" in self.driver.current_url

    @allure.title("Проверка перехода по клику на кнопку 'Лента заказов'")
    def test_click_order_feed_button(self):
        main_page = MainPage(self.driver)
        main_page.click_order_feed_button()
        assert "order-feed" in self.driver.current_url

    @allure.title("Проверка отображения всплывающего окна с деталями ингредиента")
    def test_ingredient_popup_appears(self):
        main_page = MainPage(self.driver)
        main_page.click_ingredient_button()
        assert main_page.is_ingredient_details_popup_displayed()

    @allure.title("Проверка закрытия всплывающего окна с деталями ингредиента")
    def test_close_ingredient_popup(self):
        main_page = MainPage(self.driver)
        main_page.click_ingredient_button()
        main_page.close_ingredient_details_popup()
        assert not main_page.is_ingredient_details_popup_displayed()

    @allure.title("Проверка увеличения счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self):
        main_page = MainPage(self.driver)
        initial_count = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        updated_count = main_page.get_ingredient_counter()
        assert updated_count == initial_count + 1

    @allure.title("Проверка оформления заказа для залогиненного пользователя")
    def test_logged_in_user_can_place_order(self):
        main_page = MainPage(self.driver)
        main_page.place_order()
        assert main_page.is_order_confirmation_displayed()
