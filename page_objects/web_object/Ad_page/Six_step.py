from selenium.webdriver.common.by import By

page_title = "פרסום מודעה - HomMe"

name = (By.ID, "ff_8_name_full")
phone = (By.ID, "ff_8_phone_number")
finish_button = (By.XPATH, ('//*[@id="fluentform_8"]/fieldset/div/div[2]/div[6]/div[3]/div[2]/div/button'))


class NewAdSixPage:
    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.driver.find_element(name[0], name[1])

    def get_phone(self):
        return self.driver.find_element(phone[0], phone[1])

    def finish_button(self):
        return self.driver.find_element(finish_button[0], finish_button[1])

