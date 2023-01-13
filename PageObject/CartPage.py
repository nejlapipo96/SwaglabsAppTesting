from selenium.webdriver.common.by import By

class CartPage():

    def __init__(self, driver):
        self.driver = driver

    def clickAddToCart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def clickCart(self):
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

    def clickRemove(self):
        self.driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()

    def clickContinueShopping(self):
        self.driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()

    