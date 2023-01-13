import time

from Utilities.readProperties import ReadConfig
from PageObject.LoginPage import LoginPage
from PageObject.LogoutPage import Logout

class Test_002_Logout:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_logout(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        self.logout = Logout(self.driver)
        self.logout.clickMenu()
        self.logout.clickLogoutButton()

        act_title = self.driver.title
        exp_title = "Swag Labs"
        if exp_title == act_title:
            assert True
        else:
            assert False