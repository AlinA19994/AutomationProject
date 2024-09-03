from selenium.webdriver.common.by import By

second_page_title = "פרסום מודעה - HomMe"
credits = (By.ID, "ff_8_credits")
house_commite = (By.ID, "ff_8_house_committee")
asset_tax = (By.ID, "ff_8_tax_asset")
price = (By.ID, "ff_8_price")
start_date = (By.ID, "ff_8_date_start")
next_month = (By.CLASS_NAME, "flatpickr-next-month")
apper_month = (By.CLASS_NAME, "cur-month")
apper_year = (By.CLASS_NAME, "numInput cur-year")
calender = (By.CLASS_NAME, "flatpickr-days")
popup_data = (By.XPATH, ('//div[@class="flatpickr-calendar animate arrowTop open"]'))
next_button = (By.XPATH, ('//*[@id="fluentform_8"]/fieldset/div/div[2]/div[4]/div[3]/button[2]'))


class NewAdFourthPage:
    def __init__(self, driver):
        self.driver = driver

    def get_credits(self):
        return self.driver.find_element(credits[0], credits[1])

    def get_house_commite(self):
        return self.driver.find_element(house_commite[0], house_commite[1])

    def get_asset_tax(self):
        return self.driver.find_element(asset_tax[0], asset_tax[1])

    def get_price(self):
        return self.driver.find_element(price[0], price[1])

    def get_start_date(self):
        return self.driver.find_element(start_date[0], start_date[1])

    def next_month(self):
        return self.driver.find_element(next_month[0], next_month[1])

    def get_apper_year(self):
        return self.driver.find_element(apper_year[0], apper_year[1])

    def get_apper_month(self):
        return self.driver.find_element(apper_month[0], apper_month[1])

    def calender(self):
        return self.driver.find_element(calender[0], calender[1])
    def get_next(self):
        return self.driver.find_element(next_button[0], next_button[1])