from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, "login-button").click()
