from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "button[data-test='constructor']")
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "button[data-test='order-feed']")
    INGREDIENT_BUTTON = (By.CSS_SELECTOR, "button[data-test='ingredient']")
    INGREDIENT_DETAILS_POPUP = (By.CSS_SELECTOR, "div[data-test='ingredient-details']")
    CLOSE_POPUP_BUTTON = (By.CSS_SELECTOR, "button[data-test='close-popup']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "span[data-test='ingredient-counter']")
    ADD_INGREDIENT_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-ingredient']")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button[data-test='place-order']")
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, "div[data-test='order-confirmation']")

class PasswordRecoveryPageLocators:
    RECOVERY_BUTTON = (By.CSS_SELECTOR, "button[data-test='password-recovery']")
    EMAIL_INPUT = (By.NAME, "email")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button[data-test='show-password']")

class PersonalAccountPageLocators:
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-test='account']")
    ORDER_HISTORY = (By.CSS_SELECTOR, "button[data-test='order-history']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button[data-test='logout']")

class OrderFeedPageLocators:
    ORDER_ITEM = (By.CSS_SELECTOR, "button[data-test='order-item']")
    ORDER_DETAILS_POPUP = (By.CSS_SELECTOR, "div[data-test='order-details']")
    ORDER_FEED_NAV_BUTTON = (By.CSS_SELECTOR, "button[data-test='order-feed-nav']")
    USER_ORDER = (By.CSS_SELECTOR, "div[data-test='user-order']")
    COMPLETED_ORDERS_COUNT = (By.CSS_SELECTOR, "span[data-test='completed-orders-count']")
    COMPLETED_ORDERS_TODAY_COUNT = (By.CSS_SELECTOR, "span[data-test='completed-orders-today-count']")
    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, "div[data-test='order-in-progress']")
