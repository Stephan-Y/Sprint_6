from locators.order_page_locators import OrderPageLocator
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем поле "Имя"')
    def fill_in_name_field(self, user_data):
        self.wait_element_until_visible(OrderPageLocator.USER_NAME)
        self.send_keys_to_element(OrderPageLocator.USER_NAME, user_data)

    @allure.step('Заполняем поле "Фамилия"')
    def fill_in_last_name_field(self, user_data):
        self.wait_element_until_visible(OrderPageLocator.USER_LAST_NAME)
        self.send_keys_to_element(OrderPageLocator.USER_LAST_NAME, user_data)

    @allure.step('Заполняем поле "Адрес, куда привезти заказ"')
    def fill_in_address_field(self, user_data):
        self.wait_element_until_visible(OrderPageLocator.USER_ADDRESS_OF_DELIVERY)
        self.send_keys_to_element(OrderPageLocator.USER_ADDRESS_OF_DELIVERY, user_data)

    @allure.step('Клик на поле выбора станции метро')
    def click_on_selected_metro_station(self):
        self.click_on_element(OrderPageLocator.SELECTED_METRO_STATION)

    @allure.step('Заполняем поле "Станция метро"')
    def fill_in_metro_station_field(self, user_data):
        self.wait_element_until_visible(OrderPageLocator.USER_METRO_STATION)
        self.send_keys_to_element(OrderPageLocator.USER_METRO_STATION, user_data)
        self.click_on_selected_metro_station()

    @allure.step('Заполняем поле "Номер телефона"')
    def fill_in_phone_number_field(self, user_data):
        self.wait_element_until_visible(OrderPageLocator.USER_PHONE_NUMBER)
        self.send_keys_to_element(OrderPageLocator.USER_PHONE_NUMBER, user_data)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_next_button(self):
        self.wait_element_until_visible(OrderPageLocator.NEXT_BUTTON)
        self.click_on_element(OrderPageLocator.NEXT_BUTTON)
        self.wait_element_until_visible(OrderPageLocator.HEADER_ABOUT_RENT)

    @allure.step('Заполняем форму "Кому самокат"')
    def fill_in_first_form(self, user_data):
        self.fill_in_name_field(user_data[0])
        self.fill_in_last_name_field(user_data[1])
        self.fill_in_address_field(user_data[2])
        self.fill_in_metro_station_field(user_data[3])
        self.fill_in_phone_number_field(user_data[4])

    @allure.step('Заполняем поле "Когда привезти самокат"')
    def fill_in_delivery_day_field(self, user_data):
        self.wait_element_until_visible(OrderPageLocator.DELIVERY_DAY)
        self.send_keys_to_element(OrderPageLocator.DELIVERY_DAY, user_data)
        self.click_on_element(OrderPageLocator.CLICK_ON_SELECTED_DAY)

    @allure.step('Из выпадающего списка выбираем срок аренды 1 день')
    def select_one_day_rental(self):
        self.wait_element_until_visible(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.SELECT_RENTAL_PERIOD_1_DAY)

    @allure.step('Из выпадающего списка выбираем срок аренды 2 дня')
    def select_two_days_rental(self):
        self.wait_element_until_visible(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.SELECT_RENTAL_PERIOD_2_DAYS)

    @allure.step('Из выпадающего списка выбираем срок аренды 3 дня')
    def select_three_days_rental(self):
        self.wait_element_until_visible(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.SELECT_RENTAL_PERIOD_3_DAYS)

    @allure.step('Из выпадающего списка выбираем срок аренды 4 дня')
    def select_four_days_rental(self):
        self.wait_element_until_visible(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.SELECT_RENTAL_PERIOD_4_DAYS)

    @allure.step('Из выпадающего списка выбираем срок аренды 5 дней')
    def select_five_days_rental(self, driver):
        self.wait_element_until_visible(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.SELECT_RENTAL_PERIOD_5_DAYS)

    @allure.step('Из выпадающего списка выбираем срок аренды 6 дней')
    def select_six_days_rental(self):
        self.wait_element_until_visible(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.SELECT_RENTAL_PERIOD_6_DAYS)

    @allure.step('Из выпадающего списка выбираем срок аренды 7 дней')
    def select_seven_days_rental(self):
        self.wait_element_until_visible(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.RENTAL_PERIOD_FIELD)
        self.click_on_element(OrderPageLocator.SELECT_RENTAL_PERIOD_7_DAYS)

    @allure.step('Кликаем на чекбос, выбираем серый самокат')
    def click_on_checkbox_select_grey_scooter(self):
        self.wait_element_until_visible(OrderPageLocator.CHECKBOX_GREY_SCOOTER)
        self.click_on_element(OrderPageLocator.CHECKBOX_GREY_SCOOTER)

    @allure.step('Кликаем на чекбос, выбираем черный самокат')
    def click_on_checkbox_select_black_scooter(self):
        self.wait_element_until_visible(OrderPageLocator.CHECKBOX_BLACK_SCOOTER)
        self.click_on_element(OrderPageLocator.CHECKBOX_BLACK_SCOOTER)

    @allure.step('Заполняем поле "Оставить комментарий для курьера"')
    def fill_in_leave_comment_for_courier_field(self, user_data):
        self.wait_element_until_visible(OrderPageLocator.COMMENT_FOR_COURIER)
        self.send_keys_to_element(OrderPageLocator.COMMENT_FOR_COURIER, user_data)

    @allure.step('На странице "Про аренду", под анкетой, кликаем на кнопку "Заказать"')
    def click_on_under_fields_make_order_button(self):
        self.wait_element_until_visible(OrderPageLocator.MAKE_ORDER_UNDER_FIELDS_BUTTON)
        self.click_on_element(OrderPageLocator.MAKE_ORDER_UNDER_FIELDS_BUTTON)
        self.find_element_with_wait(OrderPageLocator.POP_UP_CONFIRM_ORDER)

    @allure.step('На странице "Про аренду", в всплывающем окне подтверждения заказа, кликаем на кнопку "Да"')
    def click_on_yes_button_on_confirmation_pop_up(self):
        self.wait_element_until_visible(OrderPageLocator.POP_UP_YES_BUTTON)
        self.click_on_element(OrderPageLocator.POP_UP_YES_BUTTON)
        self.find_element_with_wait(OrderPageLocator.POP_UP_ORDER_PROCESSED)

    @allure.step('Заполняем вторую форму "Про аренду"')
    def fill_in_second_form(self, user_data):
        self.fill_in_delivery_day_field(user_data[5])
        self.select_one_day_rental()
        self.click_on_checkbox_select_black_scooter()
        self.fill_in_leave_comment_for_courier_field(user_data[6])
        self.click_on_under_fields_make_order_button()

    @allure.step('Проверяем результат')
    def check_pop_up(self):
        confirming_pop_up = self.get_text_from_element(OrderPageLocator.POP_UP_ORDER_PROCESSED)
        return confirming_pop_up == "Посмотреть статус"