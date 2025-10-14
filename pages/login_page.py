from selenium.webdriver.common.by import By

class LoginPageLocators:
    # all this variables are constant and should not be changed (that is why capitalized)
    # -- login ---
    EMAIL_FIELD = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    INVALID_CREDENTIALS_TEXT = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")
    EMAIL_EXIST_TEXT = (By.XPATH,"//p[contains(text(),'Email Address already exist!')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")


    # -- signup --
    NAME_FIELD = (By.XPATH, "//input[@placeholder='Name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[normalize-space()='Signup']")
    #SIGNUP_TEXT = (By.XPATH, "")

