import allure
import pytest
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    @allure.title('Test01: Verify Login To Website')
    @allure.description('This test verify correct login to  the website')
    def test_verify_login(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_url()
        WebFlows.verify_title()
        WebFlows.verify_user_credentials_displayed()

    @allure.title('Test03: Verify number of public ')
    @allure.description('This test verify number of element before public new ad')
    def test_verify_number_of_public_before(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_number_of_public_before()

    @allure.title('Test02: Verify create new ad')
    @allure.description('This test E2E - to create a new ad ')
    def test_create_new_add(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_url()
        WebFlows.verify_title()
        WebFlows.create_ad_first_step()
        WebFlows.create_ad_second_step()
        WebFlows.create_ad_third_step()
        WebFlows.create_ad_fourth_step()
        WebFlows.create_ad_fifth_step()
        WebFlows.create_ad_six_step()

    @allure.title('Test03: Verify number of public ')
    @allure.description('This test verify number of element after public new ad')
    def test_verify_number_of_public_after(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_number_of_public_after()


    def teardown_method(self):
        WebFlows.logout()

