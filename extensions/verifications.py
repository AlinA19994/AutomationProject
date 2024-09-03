import time

import allure
from selenium.webdriver.common.by import By
from smart_assertions import soft_assert, verify_expectations
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class Verifications:
    @staticmethod
    @allure.step('verify equals between two results')
    def verify_equals(actual, expected):
        assert actual == expected, 'Verify Equals Failed , Actual: ' + str(actual) + 'is not Equals :' + str(expected)

    @staticmethod
    @allure.step('verify if element displayed')
    def is_displayed(elem: WebElement):
        try:
            assert elem.is_displayed(), 'Verify Is displayed,Element :' + elem.text + 'Is not Displayed'
        except Exception:
            raise AssertionError('Soft Displayed Failed')

    @staticmethod
    @allure.step('verify if element enabled')
    def is_enabled(elem: WebElement):
        try:
            assert elem.is_enabled(), 'Verify Is enabled,Element :' + elem.text + 'Is not Enabled'
        except Exception:
            raise AssertionError('Soft Enabled Failed')

    @staticmethod
    @allure.step('verify if element not displayed')
    def is_not_enabled(elem: WebElement):
        try:
            assert not elem.is_enabled(), 'Verify Is displayed,Element :' + elem.text + 'Is Enable'
        except Exception:
            raise AssertionError('Soft Not Enabled Failed')

    @staticmethod
    @allure.step('verify if element displayed')
    def soft_displayed_value(elems):
        failed_elems = []
        for i in elems:
            if not i.is_displayed():
                failed_elems.append(i.get_attribute('value'))
        if len(failed_elems) > 0:
            for failed in failed_elems:
                print("Soft Displayed Failed , Elements witch have failed :'" + str(failed))
            raise AssertionError('Soft Displayed Failed')


    @staticmethod
    @allure.step('soft verification : if elements displayed on the page  ')
    def soft_displayed_text(elems):
        failed_elems = []
        for i in elems:
            try:
                if not i.is_displayed():
                    failed_elems.append(i.text)
            except NoSuchElementException:
                failed_elems.append("Element not found")
        if failed_elems:
            print("Soft Displayed Failed, Elements that failed: " + ', '.join(failed_elems))
            raise AssertionError('Soft Displayed Failed: ' + ', '.join(failed_elems))

    @staticmethod
    @allure.step('soft verification (asserts) of elements using smart-assertions')
    def soft_assert(elems):
        for i in elems:
            soft_assert(i.is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step('verify number of elements ')
    def verify_number_of_elements_in_table(table: WebElement, size):
        body = table
        tbody = body.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        # assert len(elems) == size, 'Number of elements: ' + str(len(elems)) + ' does not match expected: ' + str(size)
