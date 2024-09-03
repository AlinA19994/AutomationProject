from selenium.webdriver.common.by import By

page_title = "פרסום מודעה - HomMe"

step_progress = (By.CLASS_NAME, "ff-el-progress-status")
text_for_step = "Step 1 of 6 - כתובת הנכס"
asset_type = (By.ID, "ff_8_asset_type")
asset_status = (By.ID, "ff_8_asset_status")
city_list = (By.XPATH, ('//div[@class= "choices__list"]'))
city_dropdown = (By.XPATH, ('//div[@class = "choices__item choices__placeholder choices__item--selectable"]'))
select_city = (By.ID, "choices--ff_8_city-item-choice-2")
city_fields = (By.XPATH, ('//input[@class ="choices__input choices__input--cloned"]'))
street_dropdown = (By.XPATH, ('//div[@class= "choices__item choices__placeholder choices__item--selectable"]'))
select_street = (By.ID, "choices--ff_8_street_1-item-choice-12")
street_number = (By.ID, "ff_8_street_number")
next_button = (By.XPATH, ('//*[@class = "ff-float-right ff-btn ff-btn-next ff-btn-secondary"]'))


class NewAdFirstPage:
    def __init__(self, driver):
        self.driver = driver

    def get_step_progress(self):
        return self.driver.find_element(step_progress[0], step_progress[1])

    def get_asset_type(self):
        return self.driver.find_element(asset_type[0], asset_type[1])

    def get_asset_status(self):
        return self.driver.find_element(asset_status[0], asset_status[1])

    def get_city_list(self):
        return self.driver.find_elements(city_list[0], city_list[1])[0]

    def get_city_dropdown(self):
        return self.driver.find_elements(city_dropdown[0], city_dropdown[1])[0]

    def get_city_fields(self):
        return self.driver.find_elements(city_fields[0], city_fields[1])[0]

    def get_street_dropdown(self):
        return self.driver.find_element(street_dropdown[0], street_dropdown[1])

    def get_street_number(self):
        return self.driver.find_element(street_number[0], street_number[1])

    def get_next_button(self):
        return self.driver.find_element(next_button[0], next_button[1])

    def get_select_city(self):
        return self.driver.find_element(select_city[0], select_city[1])

    def get_select_street(self):
        return self.driver.find_element(select_street[0], select_street[1])
