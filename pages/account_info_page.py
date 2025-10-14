from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AccountInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.title_mr = (By.ID, "id_gender1")
        self.password = (By.ID, "password")
        self.days = (By.ID, "days")
        self.months = (By.ID, "months")
        self.years = (By.ID, "years")
        self.first_name = (By.ID, "first_name")
        self.last_name = (By.ID, "last_name")
        self.address = (By.ID, "address1")
        self.country = (By.ID, "country")
        self.state = (By.ID, "state")
        self.city = (By.ID, "city")
        self.zipcode = (By.ID, "zipcode")
        self.mobile = (By.ID, "mobile_number")
        self.create_button = (By.XPATH, "//button[@data-qa='create-account']")

    def fill_form(self, password, first_name, last_name, address, country, state, city, zipcode, mobile):
        self.click(*self.title_mr)
        self.send_keys(*self.password, password)
        self.send_keys(*self.first_name, first_name)
        self.send_keys(*self.last_name, last_name)
        self.send_keys(*self.address, address)
        self.send_keys(*self.country, country)
        self.send_keys(*self.state, state)
        self.send_keys(*self.city, city)
        self.send_keys(*self.zipcode, zipcode)
        self.send_keys(*self.mobile, mobile)
        self.click(*self.create_button)
