from selenium.webdriver.common.by import By


class OrderPageLocator:
    DELIVERY_DAY = [By.XPATH,
                    '//input[contains(@placeholder, "* Когда привезти самокат") and contains(@class, "Input_Responsible")]']
    CLICK_ON_SELECTED_DAY = [By.XPATH,
                             '//*[contains(@class, "react-datepicker__day react-datepicker") and contains(@class, "react-datepicker__day--selected")]']
    RENTAL_PERIOD_FIELD = [By.XPATH,
                           '//*[contains(@class, "Dropdown-placeholder") and contains(text(), "* Срок аренды")]']
    SELECT_RENTAL_PERIOD_1_DAY = [By.XPATH, '//*[contains(@class, "Dropdown-option") and contains(text(), "сутки")]']
    SELECT_RENTAL_PERIOD_2_DAYS = [By.XPATH,
                                   '//*[contains(@class, "Dropdown-option") and contains(text(), "двое суток")]']
    SELECT_RENTAL_PERIOD_3_DAYS = [By.XPATH,
                                   '//*[contains(@class, "Dropdown-option") and contains(text(), "трое суток")]']
    SELECT_RENTAL_PERIOD_4_DAYS = [By.XPATH,
                                   '//*[contains(@class, "Dropdown-option") and contains(text(), "четверо суток")]']
    SELECT_RENTAL_PERIOD_5_DAYS = [By.XPATH,
                                   '//*[contains(@class, "Dropdown-option") and contains(text(), "пятеро суток")]']
    SELECT_RENTAL_PERIOD_6_DAYS = [By.XPATH,
                                   '//*[contains(@class, "Dropdown-option") and contains(text(), "шестеро суток")]']
    SELECT_RENTAL_PERIOD_7_DAYS = [By.XPATH,
                                   '//*[contains(@class, "Dropdown-option") and contains(text(), "семеро суток")]']
    CHECKBOX_GREY_SCOOTER = [By.ID, 'grey']
    CHECKBOX_BLACK_SCOOTER = [By.ID, 'black']
    COMMENT_FOR_COURIER = [By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]']
    MAKE_ORDER_UNDER_FIELDS_BUTTON = [By.XPATH, '//button[contains(text(), "Заказать") and contains(@class, "Button_Middle")]']
    POP_UP_CONFIRM_ORDER = [By.XPATH, '//*[contains(@class, "Order_ModalHeader") and contains(text(), "Хотите оформить заказ")]']
    POP_UP_YES_BUTTON = [By.XPATH, '//button[contains(text(), "Да")]']
    POP_UP_ORDER_PROCESSED = [By.XPATH, '//*[contains(text(), "Посмотреть статус")]']
    USER_NAME = [By.XPATH, ".//input[contains(@placeholder, '* Имя')]"]
    USER_LAST_NAME = [By.XPATH, ".//input[contains(@placeholder, '* Фамилия')]"]
    USER_ADDRESS_OF_DELIVERY = [By.XPATH, ".//input[contains(@placeholder, '* Адрес: куда привезти заказ')]"]
    USER_METRO_STATION = [By.XPATH, ".//input[contains(@placeholder, '* Станция метро')]"]
    USER_PHONE_NUMBER = [By.XPATH, ".//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]"]
    NEXT_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle') and "
                             "text()='Далее']"]
    SELECTED_METRO_STATION = [By.CLASS_NAME, 'select-search__select']
    HEADER_ABOUT_RENT = [By.XPATH, '//*[contains(@class, "Order_Header") and contains(text(), "Про аренду")]']
