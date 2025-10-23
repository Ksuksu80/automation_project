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


# def remove_iframe_ads(driver):
#     """ removes iframe-adds (for example, Google Ads), if it blocks browser from clicking."""
#     try:
#         iframes = driver.find_elements(By.TAG_NAME, "iframe")
#         for frame in iframes:
#             src = frame.get_attribute("src") or ""
#             title = frame.get_attribute("title") or ""
#             if "googleads" in src or "Advertisement" in title:
#                 driver.execute_script("""
#                     var frame = arguments[0];
#                     frame.parentNode.removeChild(frame);
#                 """, frame)
#                 print("🧹 Removed advertisement iframe")
#                 return
#         print("ℹ️ No advertisement iframe found")
#     except Exception as e:
#         print(f"⚠️ Error while checking iframes: {e}")

def remove_iframe_ads(driver):
    """removes all iframe (ads), if they are present on the page."""
    try:
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        count = 0
        for iframe in iframes:
            # Проверяем, что это рекламный iframe (по src)
            src = iframe.get_attribute("src")
            if src and ("googleads" in src or "doubleclick" in src or "ad" in src):
                driver.execute_script("""
                    arguments[0].parentNode.removeChild(arguments[0]);
                """, iframe)
                count += 1
        if count > 0:
            print(f"🧹 Removed {count} advertisement iframes")
        else:
            print("ℹ️ No ad iframes found")
    except Exception as e:
        print(f"⚠️ Error while removing iframes: {e}")
