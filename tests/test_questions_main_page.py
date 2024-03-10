import pytest
from data import *
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocator


class TestQuestionsMainPage:

    @allure.title('Проверяем вопросы и ответы на главной странице')
    @allure.description(
        'Кликаем на вопросы по порядку и проверяем ответы в выпадающем списке')
    @pytest.mark.parametrize("question_num, expected_answer",
                             [(0, TrueAnswer.answer_1),
                              (1, TrueAnswer.answer_2),
                              (2, TrueAnswer.answer_3),
                              (3, TrueAnswer.answer_4),
                              (4, TrueAnswer.answer_5),
                              (5, TrueAnswer.answer_6),
                              (6, TrueAnswer.answer_7)
                              ]
    )
    def test_questions(self, driver, question_num, expected_answer):
        main_page = MainPage(driver)
        main_page.click_on_cookie_button()
        main_page.scrolling_to_questions()
        result = main_page.click_on_question_and_get_answer(MainPageLocator.QUESTION_LOCATOR, MainPageLocator.ANSWER_LOCATOR, question_num)
        assert main_page.check_answer(result, expected_answer)