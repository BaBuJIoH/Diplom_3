from locators.locators import PersonalAccountPageLocators

class PersonalAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def open_account(self):
        self.driver.find_element(*PersonalAccountPageLocators.ACCOUNT_BUTTON).click()

    def open_order_history(self):
        self.driver.find_element(*PersonalAccountPageLocators.ORDER_HISTORY).click()

    def logout(self):
        self.driver.find_element(*PersonalAccountPageLocators.LOGOUT_BUTTON).click()
