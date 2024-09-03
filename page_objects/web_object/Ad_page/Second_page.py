from selenium.webdriver.common.by import By

second_page_title = "פרסום מודעה - HomMe"
# Fields Title

floor = (By.NAME, "floor")
floors = (By.NAME, "floors")
num_rooms_drop_down = (By.ID, "ff_8_room_num")
terrace_dropdown = (By.ID, "ff_8_terrace")
parking_dropdown = (By.ID, "ff_8__parking")
build_mr = (By.ID, "ff_8_built_mr")
elevator = (By.ID, "ff_8_elevator_1")
garden_mr = (By.ID, "ff_8_garden_mr")
next_button = (By.XPATH, '//div[@data-name="form_step-8_1"]//button[@data-action="next"]')


class NewAdSecondPage:
    def __init__(self, driver):
        self.driver = driver

    def get_floor(self):
        return self.driver.find_element(floor[0], floor[1])

    def get_floors(self):
        return self.driver.find_element(floors[0], floors[1])

    def get_num_rooms_drop_down(self):
        return self.driver.find_element(num_rooms_drop_down[0], num_rooms_drop_down[1])

    def get_terrace_dropdown(self):
        return self.driver.find_element(terrace_dropdown[0], terrace_dropdown[1])

    def get_parking_dropdown(self):
        return self.driver.find_element(parking_dropdown[0], parking_dropdown[1])

    def get_build_mr(self):
        return self.driver.find_element(build_mr[0], build_mr[1])

    def get_elevator(self):
        return self.driver.find_element(elevator[0], elevator[1])

    def get_garden(self):
        return self.driver.find_element(garden_mr[0], garden_mr[1])

    def next(self):
        return self.driver.find_element(next_button[0], next_button[1])