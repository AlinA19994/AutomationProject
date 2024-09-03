from selenium.webdriver.common.by import By

wellcome_popup = (By.XPATH, '//div[@data-elementor-id="1733"]')
wellcome_popup_accept = (By.XPATH, '//div[@data-id="14e5e15"]')


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept(self):
        return self.driver.find_element(wellcome_popup_accept[0], wellcome_popup_accept[1])
