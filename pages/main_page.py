from locators.locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_constructor_button(self):
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    def click_order_feed_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_FEED_BUTTON).click()

    def click_ingredient_button(self):
        self.driver.find_element(*MainPageLocators.INGREDIENT_BUTTON).click()

    def is_ingredient_details_popup_displayed(self):
        return self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    def close_ingredient_details_popup(self):
        self.driver.find_element(*MainPageLocators.CLOSE_POPUP_BUTTON).click()

    def get_ingredient_counter(self):
        return int(self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER).text)

    def add_ingredient_to_order(self):
        self.driver.find_element(*MainPageLocators.ADD_INGREDIENT_BUTTON).click()

    def login_user(self):
        # Логика для авторизации пользователя
        pass

    def place_order(self):
        self.driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).click()

    def is_order_confirmation_displayed(self):
        return self.driver.find_element(*MainPageLocators.ORDER_CONFIRMATION).is_displayed()
