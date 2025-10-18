from pages.contact_us_page import ContactUsPageLocators as Contact_Loc
from pages.login_page import LoginPageLocators as Loc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils.helper_methods import close_banner_if_present
import time
from faker import Faker

fake = Faker()

def test_1_send_message(browser):
    # 1. verify that home page is open
    assert "Automation Exercise" in browser.title
    print("Home page opened")

    # 2. transfer to Contact us page
    browser.find_element(By.XPATH, "//a[normalize-space()='Contact us']").click()
    #WebDriverWait(browser, 7).until(EC.visibility_of_element_located(Loc.NAME_FIELD))
    #print("Contact us is opened")

    # 3. verify that "Get in touch" is visible
    header = WebDriverWait(browser,5).until(
    EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Get In Touch']")))
    assert header.is_displayed()
    print("Get in touch is visible")

    # 4. fill the application form
    name = "Kseniia Petrova"
    email = "oc2003@mail.ru"

    browser.find_element(*Contact_Loc.CONTACT_US_NAME).send_keys(name)
    browser.find_element(*Contact_Loc.CONTACT_US_EMAIL).send_keys(email)
    time.sleep(2)
    browser.find_element(*Contact_Loc.CONTACT_US_SUBJECT).send_keys("Testing contact form")
    browser.find_element(*Contact_Loc.CONTACT_US_MESSAGE).send_keys("This is a test message from automation.")
    time.sleep(2)
    browser.find_element(*Contact_Loc.CONTACT_US_SUBMIT_BUTTON).click()

    # 5. alert
    try:
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        print(f" Alert text: {alert.text}")
        alert.accept()  # press OK
        print("✅ Alert closed")
    except:
        print("ℹ️ No alert appeared after submitting the form")

    # 6. verify that the email is sent successfully
    success = WebDriverWait(browser, 7).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='status alert alert-success']"))
    )
    assert "Success! Your details have been submitted successfully." in success.text
    print("✅ Message sent successfully!")

    time.sleep(2)

    #7. Return to home page
    browser.find_element(*Contact_Loc.CONTACT_US_HOME_BUTTON ).click()

    assert "Automation Exercise" in browser.title
    print("Home page opened")





