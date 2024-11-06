import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть по элементу {locator}")
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести текст в элемент {locator}")
    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).is_displayed()

    @allure.step("Подождать {delay} секунд")
    def wait_with_delay(self, delay):
        self.driver.implicitly_wait(delay)
