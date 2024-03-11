from data import *
import allure
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Клик на "Самокат", проверяем переход на главную страницу')
    @allure.description(
        'Заполняем страницу "Для кого самокат", клик на иконку "Самокат" в хедере, проверяем переход на главную страницу')
    def test_scooter_icon(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        main_page.click_on_top_order_button()
        main_page.click_on_scooter_logo()
        assert main_page.get_img_attribute() == 'Scooter blueprint'

    @allure.title('Проверяем переход на страницу дзена по клику на "Яндек" в хедере')
    @allure.description('Клик на "Заказать", клик на иконку "Яндекс" в хедере')
    def test_click_on_yandex_icon(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        main_page.click_on_top_order_button()
        main_page.click_on_yandex_logo()
        main_page.transfer_on_last_open_window()
        main_page.wait_for_new_window(dzen)
        assert main_page.get_url() == dzen
