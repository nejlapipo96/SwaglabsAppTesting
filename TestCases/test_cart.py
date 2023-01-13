import time

from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from PageObject.LoginPage import LoginPage
from PageObject.CartPage import CartPage
from PageObject.LogoutPage import Logout
import pytest

class Test_003_Cart:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("*** Logging in ***")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("*** Successfuly logged in ***")

        self.logger.info("*** Adding and Removing Item from the Cart ***")
        self.cart = CartPage(self.driver)
        self.cart.clickAddToCart()
        self.cart.clickCart()
        self.cart.clickRemove()
        self.cart.clickContinueShopping()
        time.sleep(3)

        self.logger.info("*** Logging out ***")
        self.logout = Logout(self.driver)
        self.logout.clickMenu()
        self.logout.clickLogoutButton()

        act_title = self.driver.title
        exp_title = "Swag Labs"
        if exp_title == act_title:
            assert True
            self.logger.info("*** Test_003_Cart had Passed ***")
        else:
            self.logger.error("*** Test_003_Cart has Failed")
            assert False