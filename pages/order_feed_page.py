from locators.locators import OrderFeedPageLocators
from pages.base_page import BasePage
import allure

class OrderFeedPage(BasePage):
    @allure.step("Кликнуть на заказ")
    def click_order_item(self):
        self.click(OrderFeedPageLocators.ORDER_ITEM)

    @allure.step("Проверить, что отображается всплывающее окно с деталями заказа")
    def is_order_details_popup_displayed(self):
        return self.is_element_visible(OrderFeedPageLocators.ORDER_DETAILS_POPUP)

    @allure.step("Получить количество выполненных заказов за всё время")
    def get_completed_orders_count(self):
        return int(self.driver.find_element(*OrderFeedPageLocators.COMPLETED_ORDERS_COUNT).text)

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_completed_orders_today_count(self):
        return int(self.driver.find_element(*OrderFeedPageLocators.COMPLETED_ORDERS_TODAY_COUNT).text)
