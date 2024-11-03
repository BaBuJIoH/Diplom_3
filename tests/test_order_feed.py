import pytest
from pages.order_feed_page import OrderFeedPage

@pytest.mark.usefixtures("setup")
class TestOrderFeed:
    def test_open_order_details_popup(self):
        order_feed_page = OrderFeedPage(self.driver)
        order_feed_page.click_order_item()
        assert order_feed_page.is_order_details_popup_displayed()

    def test_user_order_displayed_in_order_feed(self):
        order_feed_page = OrderFeedPage(self.driver)
        order_feed_page.login_user()
        order_feed_page.navigate_to_order_feed()
        assert order_feed_page.is_user_order_displayed_in_feed()

    def test_completed_counter_increases_on_new_order(self):
        order_feed_page = OrderFeedPage(self.driver)
        initial_completed_count = order_feed_page.get_completed_orders_count()
        order_feed_page.create_new_order()
        assert order_feed_page.get_completed_orders_count() == initial_completed_count + 1

    def test_completed_today_counter_increases_on_new_order(self):
        order_feed_page = OrderFeedPage(self.driver)
        initial_today_count = order_feed_page.get_completed_orders_today_count()
        order_feed_page.create_new_order()
        assert order_feed_page.get_completed_orders_today_count() == initial_today_count + 1

    def test_new_order_appears_in_progress_section(self):
        order_feed_page = OrderFeedPage(self.driver)
        order_feed_page.create_new_order()
        assert order_feed_page.is_order_in_progress_section()
