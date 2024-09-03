from selenium.webdriver.common.by import By

logo = ""
about_tab = ""
apartment_tab = ""
create_sigh = ""
lease_contract_tab = ""
deal_tab = ""
contact_tab = ""
facebook_share_tab = ""
login_tab = (By.XPATH, ('//a[@class="elementor-button elementor-button-link elementor-size-sm elementor-animation-grow"]'))
create_ad_url = 'https://homme.co.il/%d7%a4%d7%a8%d7%a1%d7%95%d7%9d-%d7%9e%d7%95%d7%93%d7%a2%d7%94/'

logout_url = "https://homme.co.il/wp-login.php?action=logout&redirect_to=https%3A%2F%2Fhomme.co.il&_wpnonce=fea9680242"
confire_logout = (By.LINK_TEXT, "לצאת מהמערכת")


class UpperMenu:
    def __init__(self, driver):
        self.driver = driver

    def get_login_popup(self):
        return self.driver.find_elements(login_tab[0], login_tab[1])[0]

    def logout(self):
        return self.driver.find_element(confire_logout[0], confire_logout[1])


