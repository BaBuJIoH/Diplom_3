from locators.locators import PasswordRecoveryPageLocators

class PasswordRecoveryPage:
    def __init__(self, driver):
        self.driver = driver

    def click_recovery_button(self):
        self.driver.find_element(*PasswordRecoveryPageLocators.RECOVERY_BUTTON).click()

    def enter_email(self, email):
        self.driver.find_element(*PasswordRecoveryPageLocators.EMAIL_INPUT).send_keys(email)

    def submit_recovery(self):
        self.driver.find_element(*PasswordRecoveryPageLocators.SUBMIT_BUTTON).click()

    def toggle_password_visibility(self):
        self.driver.find_element(*PasswordRecoveryPageLocators.SHOW_PASSWORD_BUTTON).click()
