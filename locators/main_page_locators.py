from selenium.webdriver.common.by import By


class MainPageLocator:
    MAKE_ORDER_TOP_BUTTON = [By.XPATH, "//button[contains(text(), 'Статус заказа')]/preceding-sibling::button"]
    MAKE_ORDER_BOTTOM_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Middle')]"]
    COOKIE_BUTTON = [By.XPATH, '//*[@id="rcc-confirm-button"]']
    SCOOTER_ICON = [By.XPATH, '//img[@src="/assets/scooter.svg" and @alt="Scooter"]']
    IMG_MAIN_PAGE = [By.XPATH, '//img[@src="/assets/scooter.png"]']
    YANDEX_ICON = [By.XPATH, '//img[@src="/assets/ya.svg"]']
    YANDEX_SEARCHING_FIELD = [By.XPATH, '//*[contains(text(), "Поиск Яндекса")]']
    QUESTION_LOCATOR = [By.ID, "accordion__heading-{}"]
    ANSWER_LOCATOR = [By.ID, "accordion__panel-{}"]
    QUESTION_1 = [By.ID, "accordion__heading-0"]
    QUESTION_2 = [By.ID, "accordion__heading-1"]
    QUESTION_3 = [By.ID, "accordion__heading-2"]
    QUESTION_4 = [By.ID, "accordion__heading-3"]
    QUESTION_5 = [By.ID, "accordion__heading-4"]
    QUESTION_6 = [By.ID, "accordion__heading-5"]
    QUESTION_7 = [By.ID, "accordion__heading-6"]
    QUESTION_8 = [By.ID, "accordion__heading-7"]
