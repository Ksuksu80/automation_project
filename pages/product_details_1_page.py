from selenium.webdriver.common.by import By

class ProductDetails1PageLocators:
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']/h2")
    CATEGORY = (By.XPATH, "//p[contains(., 'Category:')]")
    PRICE = (By.XPATH, "//span[contains(., 'Rs.')]")
    AVAILABILITY = (By.XPATH, "//b[text()='Availability:']/parent::p")
    CONDITION = (By.XPATH, "//b[text()='Condition:']/parent::p")
    BRAND = (By.XPATH, "//b[text()='Brand:']/parent::p")