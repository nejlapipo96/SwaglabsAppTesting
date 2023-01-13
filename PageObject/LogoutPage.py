from selenium.webdriver.common.by import By

class Logout():

    def __init__(self, driver):
        self.driver = driver

    def clickMenu(self):
        self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()

    def clickLogoutButton(self):
        self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
