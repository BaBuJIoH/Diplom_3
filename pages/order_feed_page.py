from locators.locators import OrderFeedPageLocators

class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver

    def click_order_item(self):
        self.driver.find_element(*OrderFeedPageLocators.ORDER_ITEM).click()

    def is_order_details_popup_displayed(self):
        return self.driver.find_element(*OrderFeedPageLocators.ORDER_DETAILS_POPUP).is_displayed()

    def login_user(self):
        # Логика для авторизации пользователя
        pass

    def navigate_to_order_feed(self):
        self.driver.find_element(*OrderFeedPageLocators.ORDER_FEED_NAV_BUTTON).click()

    def is_user_order_displayed_in_feed(self):
        return self.driver.find_element(*OrderFeedPageLocators.USER_ORDER).is_displayed()

    def get_completed_orders_count(self):
        return int(self.driver.find_element(*OrderFeedPageLocators.COMPLETED_ORDERS_COUNT).text)

    def create_new_order(self):
        # Логика для создания нового заказа
        pass

    def get_completed_orders_today_count(self):
        return int(self.driver.find_element(*OrderFeedPageLocators.COMPLETED_ORDERS_TODAY_COUNT).text)

    def is_order_in_progress_section(self):
        return self.driver.find_element(*OrderFeedPageLocators.ORDER_IN_PROGRESS).is_displayed()
