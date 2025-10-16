from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def close_banner_if_present(driver):
    """It closes banner."""
    possible_selectors = [
        ".cookie-banner", ".popup", ".overlay", ".modal", ".banner", "#cookie", ".close-btn"
    ]
    for selector in possible_selectors:
        try:
            elem = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
            )
            driver.execute_script("arguments[0].click();", elem)
            print(f"banner is closed: {selector}")
            return
        except:
            pass
    print("banner is not found —test continues.")
