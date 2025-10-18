from selenium.webdriver.common.by import By

class ContactUsPageLocators:
    CONTACT_US_NAME = (By.XPATH, "//input[@placeholder='Name']")
    CONTACT_US_EMAIL = (By.XPATH, "//input[@placeholder='Email']")
    CONTACT_US_SUBJECT = (By.XPATH, "//input[@placeholder='Subject']")
    CONTACT_US_MESSAGE = (By.XPATH, "//textarea[@id='message']")
    CONTACT_US_SELECT_FILE = (By.XPATH, "//input[@name='upload_file']")
    CONTACT_US_SUBMIT_BUTTON = (By.XPATH, "//input[@name='submit']")
    CONTACT_US_HOME_BUTTON = (By.XPATH, "//span[normalize-space()='Home']")





