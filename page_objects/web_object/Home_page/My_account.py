from selenium.webdriver.common.by import By

my_account_url = 'https://homme.co.il/%D7%94%D7%97%D7%A9%D7%91%D7%95%D7%9F-%D7%A9%D7%9C%D7%99/'
my_account_title = "החשבון שלי - HomMe"
user_name = (By.XPATH, ("//li[text()= ' tester']"))
email = (By.XPATH, ("//li[text()= ' smartypurchase@gmail.com']"))

manage_my_ads_button = (By.XPATH, ("//div[@data-id= '98ab858']"))
my_public = (By.XPATH, ('//*[starts-with(@class, "jet-listing-grid__item jet-listing-dynamic")]'))




class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(user_name[0], user_name[1])

    def get_email(self):
        return self.driver.find_element(email[0], email[1])

    def get_my_public(self):
        return self.driver.find_elements(my_public[0], my_public[1])




