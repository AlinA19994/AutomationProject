from selenium.webdriver.common.by import By

login_popup = (By.XPATH, '//div[@data-id="d21758b"]')
user_name = (By.ID, 'user-d21758b')
password = (By.ID, 'password-d21758b')
remember_me_checkbox = (By.ID, 'elementor-login-remember-me')
login_button = (By.NAME, "wp-submit")
forgot_password = (By.CLASS_NAME, "elementor-lost-password")
sigh_up = (By.CLASS_NAME, "elementor-register")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_field(self):
        return self.driver.find_element(user_name[0], user_name[1])

    def get_password_field(self):
        return self.driver.find_element(password[0], password[1])

    def get_login_button(self):
        return self.driver.find_element(login_button[0], login_button[1])

    def get_remember_me(self):
        return self.driver.find_element(remember_me_checkbox[0], remember_me_checkbox[1])

    def get_forgot_password(self):
        return self.driver.find_element(forgot_password[0], forgot_password[1])

    def get_sigh_up(self):
        return self.driver.find_element(sigh_up[0], sigh_up[1])



