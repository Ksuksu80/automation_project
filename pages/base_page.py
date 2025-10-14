# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click(self, locator_type, locator):
#         self.driver.find_element(locator_type, locator).click()
#
#     def send_keys(self, locator_type, locator, text):
#         self.driver.find_element(locator_type, locator).send_keys(text)
#
#     # def click(self, locator_type, locator):
#     #     WebDriverWait(self.driver, 10).until(
#     #         EC.element_to_be_clickable((locator_type, locator))
#     #     ).click()
#
#     def get_text(self, locator_type, locator):
#         return self.driver.find_element(locator_type, locator).text
