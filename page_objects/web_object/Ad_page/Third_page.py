from selenium.webdriver.common.by import By

page_title = "פרסום מודעה - HomMe"
# Fields titles:
asset_characteristics = (By.XPATH, ('//label[@aria-label="מאפייני הנכס"]'))
container_fieldset = (By.CLASS_NAME, "ff_el_checkable_photo_holders")
about_asset = (By.XPATH, ('//label[@for="ff_8_asset_description"]'))
container_imgs = (By.CLASS_NAME, "ff-el-image-input-src")
about_textarea = (By.ID, "ff_8_asset_description")
next_button = (By.XPATH, '//*[@id="fluentform_8"]/fieldset/div/div[2]/div[3]/div[3]/button[2]')


class NewAdThirdPage:
    def __init__(self, driver):
        self.driver = driver

    def get_asset_characteristics(self):
        return self.driver.find_element(asset_characteristics[0], asset_characteristics[1])

    def get_container_fieldset(self):
        return self.driver.find_element(container_fieldset[0], container_fieldset[1])

    def get_about_asset(self):
        return self.driver.find_element(about_asset[0], about_asset[1])

    def get_container_imgs(self):
        return self.driver.find_elements(container_imgs[0], container_imgs[1])

    def get_about_textarea(self):
        return self.driver.find_element(about_textarea[0], about_textarea[1])

    def get_next(self):
        return self.driver.find_element(next_button[0], next_button[1])