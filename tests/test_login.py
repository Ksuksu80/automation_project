from pages.login_page import LoginPageLocators as Loc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils.helper_methods import close_banner_if_present, remove_iframe_ads
from selenium.common.exceptions import ElementClickInterceptedException
import time
from faker import Faker

fake = Faker()

def test_1_register_user(browser):
    # register a new user
    # 1. verify that home page is open
    assert "Automation Exercise" in browser.title
    print("Home page opened")

    browser.find_element(By.XPATH, "//a[@href='/login']").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Loc.NAME_FIELD))
    print("Signup / Login page opened")
    # 2. Type in "New User Signup!"
    name = fake.first_name()
    email = fake.unique.email()

    browser.find_element(*Loc.NAME_FIELD).send_keys(name)
    browser.find_element(*Loc.SIGNUP_EMAIL).send_keys(email)
    browser.find_element(*Loc.SIGNUP_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Enter Account Information')]")))
    print("✅ Account info form is visible")

    # 3. type the application in

    browser.find_element(By.ID, "password").send_keys("Qwerty123!")
    time.sleep(3)

    Select(browser.find_element(By.ID, "days")).select_by_visible_text("10")
    Select(browser.find_element(By.ID, "months")).select_by_visible_text("May")
    Select(browser.find_element(By.ID, "years")).select_by_visible_text("1995")
    # 4. close banner if it exists
    time.sleep(3)
    close_banner_if_present(browser)
    remove_iframe_ads(browser)
    try:
         checkbox_newsletter = browser.find_element(By.XPATH, "//input[@id='newsletter']")
         checkbox_newsletter.click()
    except ElementClickInterceptedException:
         print("Click intercepted on newsletter checkbox — retry with JS")
         remove_iframe_ads(browser)
         browser.execute_script("arguments[0].click();", checkbox_newsletter)

    # mark checkboxes
    # checkbox = browser.find_element(By.XPATH, "//input[@id='newsletter']")
    # checkbox.click()
    # checkbox_optin = browser.find_element(By.XPATH, "//input[@id='optin']")
    # checkbox_optin.click()
    close_banner_if_present(browser)
    remove_iframe_ads(browser)
    time.sleep(3)
    try:
        checkbox_optin = browser.find_element(By.XPATH, "//input[@id='optin']")
        checkbox_optin.click()
    except ElementClickInterceptedException:
        print("Click intercepted on optin checkbox — retry with JS")
        remove_iframe_ads(browser)
        browser.execute_script("arguments[0].click();", checkbox_optin)
    time.sleep(3)

    browser.find_element(By.ID, "first_name").send_keys(name)
    browser.find_element(By.ID, "last_name").send_keys(fake.last_name())
    browser.find_element(By.ID, "address1").send_keys("8900 Brunswick st")

    Select(browser.find_element(By.ID, "country")).select_by_visible_text("United States")

    browser.find_element(By.ID, "state").send_keys("California")
    browser.find_element(By.ID, "city").send_keys("San Diego")
    browser.find_element(By.ID, "zipcode").send_keys("92101")
    browser.find_element(By.ID, "mobile_number").send_keys("3473561000")
    # remove_iframe_ads(browser)
    # time.sleep(3)
    # browser.find_element(By.XPATH, "//button[@data-qa='create-account']").click()
    create_button = browser.find_element(By.XPATH, "//button[@data-qa='create-account']")
    try:
        create_button.click()
    except ElementClickInterceptedException:
        print("⚠️ Click intercepted on create-account — retrying after cleaning ads")
        remove_iframe_ads(browser)
        browser.execute_script("arguments[0].scrollIntoView(true);", create_button)
        time.sleep(1)
        browser.execute_script("arguments[0].click();", create_button)
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "ACCOUNT CREATED!"))

    print("Account created successfully!")


def test_2_login(browser):
    # log in as user
    # 1. verify that home page is open
    assert "Automation Exercise" in browser.title
    print("Home page opened")

    browser.find_element(By.XPATH, "//a[@href='/login']").click()
    time.sleep(6)
    # WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located(Loc.NAME_FIELD))

    print("Signup / Login page opened")
    # 2. Type in "Login!"

    email = "oc2002@inbox.ru"
    password = "Fuggy_1$hug"
    browser.find_element(*Loc.EMAIL_FIELD).send_keys(email)
    browser.find_element(*Loc.PASSWORD_FIELD).send_keys(password)
    browser.find_element(*Loc.LOGIN_BUTTON).click()
    time.sleep(6)

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Loc.LOGGED_IN_TEXT))
    logged_text = browser.find_element(*Loc.LOGGED_IN_TEXT).text
    print(f" {logged_text} is visible")
    assert "Logged in as" in logged_text

def test_3_invalid_password(browser):
    # log in as user with invalid password
    # 1. verify that home page is open
    assert "Automation Exercise" in browser.title
    print("Home page opened")

    browser.find_element(By.XPATH, "//a[@href='/login']").click()
    time.sleep(3)
    # WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located(Loc.NAME_FIELD))

    print("Signup / Login page opened")
    # 2. Type in "Login!"

    email = "oc2002@inbox.ru"
    password = "12345678"
    browser.find_element(*Loc.EMAIL_FIELD).send_keys(email)
    browser.find_element(*Loc.PASSWORD_FIELD).send_keys(password)
    browser.find_element(*Loc.LOGIN_BUTTON).click()
    time.sleep(3)

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Loc.INVALID_CREDENTIALS_TEXT))
    error_text = browser.find_element(*Loc.INVALID_CREDENTIALS_TEXT).text
    print(f" {error_text} is visible")
    assert "Your email or password is incorrect!" in error_text

def test_4_logout(browser):
    # log in as user
    # 1. verify that home page is open
    assert "Automation Exercise" in browser.title
    print("Home page opened")

    browser.find_element(By.XPATH, "//a[@href='/login']").click()
    time.sleep(6)
    # WebDriverWait(browser, 10).until(
    #     EC.visibility_of_element_located(Loc.NAME_FIELD))

    print("Signup / Login page opened")
    # 2. Type in "Login!"

    email = "oc2002@inbox.ru"
    password = "Fuggy_1$hug"
    browser.find_element(*Loc.EMAIL_FIELD).send_keys(email)
    browser.find_element(*Loc.PASSWORD_FIELD).send_keys(password)
    browser.find_element(*Loc.LOGIN_BUTTON).click()
    time.sleep(6)

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Loc.LOGGED_IN_TEXT))
    logged_text = browser.find_element(*Loc.LOGGED_IN_TEXT).text
    print(f" {logged_text} is visible")
    assert "Logged in as" in logged_text

    #logout the account
    browser.find_element(*Loc.LOGOUT_BUTTON).click()
    # verify that browser returned to home page
    assert "Automation Exercise" in browser.title
    print("Home page opened")

def test_5_register_with_existing_email(browser):
    # register with existing user email
    # 1. verify that home page is open
    assert "Automation Exercise" in browser.title
    print("Home page opened")

    browser.find_element(By.XPATH, "//a[@href='/login']").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Loc.NAME_FIELD))
    print("Signup / Login page opened")
    # 2. Type in "New User Signup!"
    name = "Kseniia Petrova"
    email = "oc2002@inbox.ru"

    browser.find_element(*Loc.NAME_FIELD).send_keys(name)
    browser.find_element(*Loc.SIGNUP_EMAIL).send_keys(email)
    browser.find_element(*Loc.SIGNUP_BUTTON).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Loc.EMAIL_EXIST_TEXT))
    error_2_text = browser.find_element(*Loc.EMAIL_EXIST_TEXT).text
    print(f" {error_2_text} is visible")
    assert "Email Address already exist!" in error_2_text

# delete_button = WebDriverWait(browser, 10).until(
    # EC.element_to_be_clickable((By.XPATH, "//a[@href='/delete_account']")))
    # delete_button.click()
    #
    # #  verify that account is deleted
    # WebDriverWait(browser, 10).until(
    # EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "ACCOUNT DELETED!"))
    # print("✅ Account deleted successfully!")
    # time.sleep(3)

