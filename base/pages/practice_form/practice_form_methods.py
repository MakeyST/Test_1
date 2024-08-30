import time
from pstats import Stats

import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)

        try:
            with allure.step("Ввод имени и фамилии"):
                practice_form.first_name.fill(practice_form.Name_text)
                practice_form.last_name.fill("Иванов")

        except AssertionError as e:
            errors.append(str(e))
