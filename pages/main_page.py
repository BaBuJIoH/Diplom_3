from locators.locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient_button(self):
        self.click(MainPageLocators.INGREDIENT_BUTTON)

    @allure.step("Проверить, что отображается всплывающее окно с деталями ингредиента")
    def is_ingredient_details_popup_displayed(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step("Закрыть всплывающее окно с деталями ингредиента")
    def close_ingredient_details_popup(self):
        self.click(MainPageLocators.CLOSE_POPUP_BUTTON)

    @allure.step("Получить количество ингредиентов в заказе")
    def get_ingredient_counter(self):
        return int(self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER).text)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self):
        self.click(MainPageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Проверить, что отображается подтверждение заказа")
    def is_order_confirmation_displayed(self):
        return self.is_element_visible(MainPageLocators.ORDER_CONFIRMATION)
