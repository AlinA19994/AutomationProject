import time

import allure
from selenium.common import StaleElementReferenceException

from extensions.ui_actions import UiActions
import utilities.manage_page as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data
from page_objects.web_object.Home_page.Login_page import login_popup
from page_objects.web_object.Home_page.Home_page import wellcome_popup
from page_objects.web_object.Home_page.My_account import my_account_title, my_account_url
from page_objects.web_object.Home_page.Upper_menu import create_ad_url, logout_url, confire_logout
from page_objects.web_object.Ad_page.First_page import page_title
from page_objects.web_object.Ad_page.Second_page import second_page_title, next_button
from page_objects.web_object.Ad_page.Fifth_page import upload_file


about_asset_text = "דירת גן 3 חדרים כולל ממד באם המושבות הוותיקה. רחוב חד סטרי שקט. מטבח גדול משודרג, חדר רחצה + " \
                   "שירותי אורחים. מיזוג מרכזי + מזגנים בחדרים. חימום סולארי, אינטרנט מהיר. חצר 120 מר עם יציאה לחצר " \
                   "גם מחדר שינה לרחבת בטון - אפשרות לסגור לחדרון. פרגולה, מחסן, עצי נוי ופרי. סורגים + תריס פלדה חדש " \
                   "ביציאה לחצר. חניה צמודה. הליכה קצרה למרכז המסחרי. קרוב לתחנת רכבת קרית אריה ורכבת קלה. ארנונה: " \
                   "740 לחודשיים. "

number_of_public_before = None
number_of_public_after = None

class WebFlows:
    @staticmethod
    @allure.step('Login to web site')
    def login_flow(user: str, password: str):
        try:
            wait(For.ELEMENT_DISPLAYED, wellcome_popup)
            UiActions.click(page.home_page.accept())
            UiActions.click(page.home_page_upper_menu.get_login_popup())
        except:
            UiActions.click(page.home_page_upper_menu.get_login_popup())
        wait(For.ELEMENT_TO_BE_CLICKABLE, login_popup)
        UiActions.update_text(page.home_page_login_popup.get_user_field(), user)
        UiActions.update_text(page.home_page_login_popup.get_password_field(), password)
        UiActions.click(page.home_page_login_popup.get_login_button())

    @staticmethod
    def logout():
        UiActions.navigate_to_url(logout_url)
        wait(For.ELEMENT_TO_BE_CLICKABLE, confire_logout)
        UiActions.click(page.home_page_upper_menu.logout())
        UiActions.clear_cookie()
        UiActions.navigate_to_url(get_data('Url'))

    @staticmethod
    @allure.step('Verify correct url')
    def verify_url():
        actual_url = UiActions.current_url()
        Verifications.verify_equals(actual_url, my_account_url)

    @staticmethod
    @allure.step('Verify url title')
    def verify_title():
        actual_title = UiActions.current_title()
        Verifications.verify_equals(actual_title, my_account_title)

    @staticmethod
    @allure.step('verify login -  in My account tab displayed my credentials ')
    def verify_user_credentials_displayed():
        Verifications.is_displayed(page.my_account_page.get_user_name())
        Verifications.is_displayed(page.my_account_page.get_email())

    @staticmethod
    @allure.step('step 1/6 - to create a new ad ')
    def create_ad_first_step():
        UiActions.clear_cookie()
        UiActions.navigate_to_url(create_ad_url)
        # Verify Correct Title :
        actual_title = UiActions.current_title()
        Verifications.verify_equals(actual_title, page_title)
        # Verify Element Displayed:
        elems = [page.new_ad_first_page.get_asset_type(),
                 page.new_ad_first_page.get_asset_status(),
                 page.new_ad_first_page.get_city_dropdown(),
                 page.new_ad_first_page.get_street_number()
                 ]
        Verifications.soft_displayed_text(elems)
        UiActions.select_by_value(page.new_ad_first_page.get_asset_type(), "דירת גן")
        UiActions.select_by_value(page.new_ad_first_page.get_asset_status(), "משופץ")
        UiActions.click(page.new_ad_first_page.get_city_dropdown())
        UiActions.click(page.new_ad_first_page.get_select_city())
        time.sleep(1)
        Verifications.is_displayed(page.new_ad_first_page.get_street_dropdown())
        UiActions.click(page.new_ad_first_page.get_street_dropdown())
        time.sleep(1)
        UiActions.click(page.new_ad_first_page.get_select_street())
        UiActions.clear(page.new_ad_first_page.get_street_number())
        UiActions.update_text(page.new_ad_first_page.get_street_number(), "9/1")
        time.sleep(3)
        UiActions.click(page.new_ad_first_page.get_next_button())

    @staticmethod
    @allure.step('step 2/6 - to create a new ad ')
    def create_ad_second_step():
        UiActions.clear_cookie()
        time.sleep(1)
        # Verify Tile :
        actual_title = UiActions.current_title()
        Verifications.verify_equals(actual_title, second_page_title)
        # Verify Element Displayed:
        elems = [page.new_ad_second_page.get_floor(),
                 page.new_ad_second_page.get_floors(),
                 page.new_ad_second_page.get_num_rooms_drop_down(),
                 page.new_ad_second_page.get_terrace_dropdown(),
                 page.new_ad_second_page.get_parking_dropdown(),
                 page.new_ad_second_page.get_build_mr(),
                 page.new_ad_second_page.get_elevator(),
                 page.new_ad_second_page.get_garden()
                 ]
        Verifications.soft_displayed_text(elems)
        UiActions.update_text(page.new_ad_second_page.get_floor(), 7)
        UiActions.update_text(page.new_ad_second_page.get_floors(), 10)
        UiActions.select_by_value(page.new_ad_second_page.get_num_rooms_drop_down(), "3.5")
        UiActions.select_by_value(page.new_ad_second_page.get_terrace_dropdown(), "1")
        UiActions.select_by_value(page.new_ad_second_page.get_parking_dropdown(), "2")
        UiActions.update_text(page.new_ad_second_page.get_build_mr(), "75")
        UiActions.select_by_value(page.new_ad_second_page.get_elevator(), "עם")
        wait(For.ELEMENT_TO_BE_CLICKABLE, next_button)
        UiActions.click(page.new_ad_second_page.next())

    @staticmethod
    @allure.step('step 3/6 - to create a new ad ')
    def create_ad_third_step():
        UiActions.clear_cookie()
        time.sleep(1)
        # Verify Tile :
        actual_title = UiActions.current_title()
        Verifications.verify_equals(actual_title, second_page_title)
        # Verify Element Displayed:
        elem = [
            page.new_ad_third_page.get_asset_characteristics(),
            page.new_ad_third_page.get_container_fieldset(),
            page.new_ad_third_page.get_about_asset()
        ]
        Verifications.soft_displayed_text(elem)
        UiActions.clicks_on_imgs(page.new_ad_third_page.get_container_imgs())
        UiActions.update_text(page.new_ad_third_page.get_about_textarea(), about_asset_text)
        UiActions.click(page.new_ad_third_page.get_next())

    @staticmethod
    @allure.step('step 4/6 - to create a new ad ')
    def create_ad_fourth_step():
        UiActions.clear_cookie()
        time.sleep(1)
        # Verify Tile :
        actual_title = UiActions.current_title()
        Verifications.verify_equals(actual_title, second_page_title)
        # Verify Element Displayed:
        elems = [
            page.new_ad_fourth_page.get_credits(),
            page.new_ad_fourth_page.get_house_commite(),
            page.new_ad_fourth_page.get_asset_tax(),
            page.new_ad_fourth_page.get_price(),
            page.new_ad_fourth_page.get_start_date()
        ]
        Verifications.soft_displayed_text(elems)
        UiActions.update_text(page.new_ad_fourth_page.get_credits(), 12)
        UiActions.update_text(page.new_ad_fourth_page.get_house_commite(), 100)
        UiActions.update_text(page.new_ad_fourth_page.get_asset_tax(), 550)
        UiActions.update_text(page.new_ad_fourth_page.get_price(), 3500)
        UiActions.data_picker(page.new_ad_fourth_page.get_start_date(),
                              page.new_ad_fourth_page.get_apper_month(),
                              "February",
                              page.new_ad_fourth_page.next_month(),
                              page.new_ad_fourth_page.calender(),
                              "15")
        time.sleep(5)
        UiActions.click(page.new_ad_fourth_page.get_next())
        time.sleep(3)

    @staticmethod
    @allure.step('step 5/6 - to create a new ad ')
    def create_ad_fifth_step():
        UiActions.clear_cookie()
        time.sleep(1)
        # Verify Tile :
        actual_title = UiActions.current_title()
        Verifications.verify_equals(actual_title, second_page_title)
        # Verify Element Displayed:
        elems = [
            page.new_ad_fifth_page.get_upload_file()
        ]
        Verifications.soft_displayed_text(elems)
        try:
            UiActions.upload_file(page.new_ad_fifth_page.get_upload_file(), get_data('First_Img'))
        except StaleElementReferenceException:
            wait(For.ELEMENT_TO_BE_CLICKABLE, upload_file)
        try:
            UiActions.upload_file(page.new_ad_fifth_page.get_upload_file(), get_data('Second_Img'))
        except StaleElementReferenceException:
            wait(For.ELEMENT_TO_BE_CLICKABLE, upload_file)

        imgs = [
            page.new_ad_fifth_page.get_first_img(),
            page.new_ad_fifth_page.get_second_img()
        ]
        Verifications.soft_displayed_text(imgs)
        time.sleep(10)  # wait to upload files
        UiActions.click(page.new_ad_fifth_page.get_next_button())
        time.sleep(2)

    @staticmethod
    @allure.step('step 6/6 - to create a new ad ')
    def create_ad_six_step():
        UiActions.clear_cookie()
        time.sleep(1)
        # Verify Tile :
        actual_title = UiActions.current_title()
        Verifications.verify_equals(actual_title, second_page_title)
        # Verify Element Displayed:
        elems = [
            page.new_ad_six_page.get_name(),
            page.new_ad_six_page.get_phone()
        ]
        Verifications.soft_displayed_text(elems)
        UiActions.update_text(page.new_ad_six_page.get_name(), "a")
        UiActions.update_text(page.new_ad_six_page.get_phone(), "05287451111")
        UiActions.click(page.new_ad_six_page.finish_button())


    @staticmethod
    @allure.step('Step: counting elements before ')
    def verify_number_of_public_before():
        globals()['number_of_public_before'] = int(UiActions.count_of_element(page.my_account_page.get_my_public()))

    @staticmethod
    @allure.step('Step: verify element after public new ad ')
    def verify_number_of_public_after():
        globals()['number_of_public_after'] = int(UiActions.count_of_element(page.my_account_page.get_my_public()))
        expect = number_of_public_before + 1
        Verifications.verify_equals(number_of_public_after, expect)





