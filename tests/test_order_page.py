import pytest
from data import *
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Заполняем форму пользователя, проверяем переход на следующую страницу')
    @allure.description(
        'Запустили браузер, клик на "Заказать" в хедере страницы, заполнили форму клиента, клик "Далее", проверяем '
        'переход на следующую страницу "Про аренду"')
    @pytest.mark.parametrize("user_data", [positive_user_data_1, positive_user_data_2])
    def test_positive_make_order_click_on_top_button(self, driver, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_cookie_button()
        main_page.click_on_top_order_button()
        order_page.fill_in_first_form(user_data)
        order_page.click_on_next_button()
        order_page.fill_in_second_form(user_data)
        order_page.click_on_yes_button_on_confirmation_pop_up()
        assert order_page.check_pop_up()


    @allure.title('Заполняем форму пользователя, проверяем переход на следующую страницу')
    @allure.description(
        'Запустили браузер, клик на "Заказать" внизу страницы, заполнили форму клиента, клик "Далее", проверяем '
        'переход на следующую страницу "Про аренду"')
    @pytest.mark.parametrize("user_data", [positive_user_data_1, positive_user_data_2])
    def test_positive_make_order_click_on_top_button(self, driver, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_cookie_button()
        main_page.click_on_bottom_order_button()
        order_page.fill_in_first_form(user_data)
        order_page.click_on_next_button()
        order_page.fill_in_second_form(user_data)
        order_page.click_on_yes_button_on_confirmation_pop_up()
        assert order_page.check_pop_up()
