from selenium.webdriver.common.by import By

second_page_title = "פרסום מודעה - HomMe"
upload_file = (By.ID, "ff_8_pictures_1")
imgs_list = (By.CLASS_NAME, "ff-uploaded-list")
first_img = (By.CLASS_NAME, "ff-upload-details")
second_img = (By.CLASS_NAME, "ff-upload-details")

first_complete = (By.XPATH, ('//*[text()= "100% Completed"]'))
second_complete = (By.XPATH, ('//*[text()= "100% Completed"]'))
next_button = (By.XPATH, ('//*[@id="fluentform_8"]/fieldset/div/div[2]/div[5]/div[2]/button[2]'))


class NewAdFifthPage:
    def __init__(self, driver):
        self.driver = driver

    def get_upload_file(self):
        return self.driver.find_element(upload_file[0], upload_file[1])

    def get_next_button(self):
        return self.driver.find_element(next_button[0], next_button[1])

    def get_first_img(self):
        return self.driver.find_elements(first_img[0], first_img[1])[0]

    def get_second_img(self):
        return self.driver.find_element(second_img[0], second_img[1])

