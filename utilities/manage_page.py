import test_cases.conftest as conf

#WEB#
from page_objects.web_object.Ad_page.Fifth_page import NewAdFifthPage
from page_objects.web_object.Ad_page.First_page import NewAdFirstPage
from page_objects.web_object.Ad_page.Fourth_page import NewAdFourthPage
from page_objects.web_object.Ad_page.Second_page import NewAdSecondPage
from page_objects.web_object.Ad_page.Six_step import NewAdSixPage
from page_objects.web_object.Ad_page.Third_page import NewAdThirdPage
from page_objects.web_object.Home_page.Home_page import HomePage
from page_objects.web_object.Home_page.Login_page import LoginPage
from page_objects.web_object.Home_page.My_account import MyAccountPage
from page_objects.web_object.Home_page.Upper_menu import UpperMenu


#WebObjects


home_page = None
home_page_upper_menu = None
home_page_login_popup = None
my_account_page = None
new_ad_first_page = None
new_ad_second_page = None
new_ad_third_page = None
new_ad_fourth_page = None
new_ad_fifth_page = None
new_ad_six_page = None






class ManagerPages:
    @staticmethod
    def init_web_pages():
        globals()['home_page'] = HomePage(conf.web_driver)
        globals()['home_page_upper_menu'] = UpperMenu(conf.web_driver)
        globals()['home_page_login_popup'] = LoginPage(conf.web_driver)
        globals()['my_account_page'] = MyAccountPage(conf.web_driver)
        globals()['new_ad_first_page'] = NewAdFirstPage(conf.web_driver)
        globals()['new_ad_second_page'] = NewAdSecondPage(conf.web_driver)
        globals()['new_ad_third_page'] = NewAdThirdPage(conf.web_driver)
        globals()['new_ad_fourth_page'] = NewAdFourthPage(conf.web_driver)
        globals()['new_ad_fifth_page'] = NewAdFifthPage(conf.web_driver)
        globals()['new_ad_six_page'] = NewAdSixPage(conf.web_driver)
