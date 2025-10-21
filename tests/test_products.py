from pages.products_page import ProductsPageLocators as Prod_Loc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.product_details_1_page import ProductDetails1PageLocators as ProdDetails1Loc
from utils.helper_methods import close_banner_if_present, remove_iframe_ads
from selenium.common.exceptions import ElementClickInterceptedException
import time

def test_1_verify_all_products_and_details(browser):

    # 1. verify that home page is open
    assert "Automation Exercise" in browser.title
    print("Home page opened")

    """transfer to products page"""
    browser.find_element(By.XPATH, "//a[@href='/products']").click()
    # WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Loc.NAME_FIELD))
    # print("Products page opened")
    time.sleep(3)

    # verify that "All PRODUCTS" is visible
    header = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='All Products']")))
    assert header.is_displayed()
    print("All PRODUCTS is visible")

    # removes iframe
    remove_iframe_ads(browser)
    time.sleep(2)
    close_banner_if_present(browser)

    # select 1st product and click on View product
    product_link = browser.find_element(*Prod_Loc.VIEW_PRODUCT_1)
    try:
        product_link.click()
    except ElementClickInterceptedException:
        print("⚠️ Click intercepted — removing iframe again and using JS click")
        remove_iframe_ads(browser)
        browser.execute_script("arguments[0].click();", product_link)

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Blue Top']"))
    )

    # verify that product name, category, price, availability, condition, brand are visible

    assert browser.find_element(*ProdDetails1Loc.PRODUCT_NAME).is_displayed()
    assert browser.find_element(*ProdDetails1Loc.CATEGORY).is_displayed()
    assert browser.find_element(*ProdDetails1Loc.PRICE).is_displayed()
    assert browser.find_element(*ProdDetails1Loc.AVAILABILITY).is_displayed()
    assert browser.find_element(*ProdDetails1Loc.CONDITION).is_displayed()
    assert browser.find_element(*ProdDetails1Loc.BRAND).is_displayed()

    print("✅ All product details are displayed correctly")




