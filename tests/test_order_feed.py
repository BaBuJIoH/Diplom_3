import pytest
import allure
from pages.order_feed_page import OrderFeedPage
from locators.locators import OrderFeedPageLocators

@pytest.mark.usefixtures("setup")
class TestOrderFeed:

    @allure.title("Проверка открытия всплывающего окна с деталями заказа при клике на заказ")
    def test_order_details_popup(self):
        order_feed_page = OrderFeedPage(self.driver)
        order_feed_page.click_order_item()
        assert order_feed_page.is_order_details_popup_displayed()

    @allure.title("Проверка отображения заказов пользователя в разделе 'История заказов'")
    def test_user_orders_displayed_in_order_feed(self):
        order_feed_page = OrderFeedPage(self.driver)
        assert order_feed_page.is_element_visible(OrderFeedPageLocators.USER_ORDER)

    @allure.title("Проверка увеличения счетчика выполненных заказов за всё время при создании нового заказа")
    def test_completed_orders_count_increases(self):
        order_feed_page = OrderFeedPage(self.driver)
        initial_count = order_feed_page.get_completed_orders_count()
        # Add order creation here
        updated_count = order_feed_page.get_completed_orders_count()
        assert updated_count == initial_count + 1

    @allure.title("Проверка увеличения счетчика выполненных заказов за сегодня при создании нового заказа")
    def test_completed_orders_today_count_increases(self):
        order_feed_page = OrderFeedPage(self.driver)
        initial_today_count = order_feed_page.get_completed_orders_today_count()
        # Add order creation here
        updated_today_count = order_feed_page.get_completed_orders_today_count()
        assert updated_today_count == initial_today_count + 1

    @allure.title("Проверка появления заказа в разделе 'В работе' после его оформления")
    def test_order_appears_in_progress_section(self):
        order_feed_page = OrderFeedPage(self.driver)
        # Add order creation here
        assert order_feed_page.is_element_visible(OrderFeedPageLocators.ORDER_IN_PROGRESS)
