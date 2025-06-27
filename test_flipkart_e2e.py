import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.mark.e2e_flipkart
def test_flipkart_shopping_flow(driver):
    wait = WebDriverWait(driver, 5)
    driver.get("https://www.flipkart.com")

    # Close login popup if present
    try:
        close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'✕')]")))
        close_btn.click()
    except:
        pass

    # Click login
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Login')]")))
    login_btn.click()

    # Enter credentials (replace with your test account)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='r4vIwl BV+Dqf']"))).send_keys("Enter your phone number")
    # driver.find_element(By.XPATH, "//input[@type='password']").send_keys("test_password")
    driver.find_element(By.XPATH, "//button[contains(text(),'Request OTP')]").click()
    # Enter OTP (replace with your test OTP)
    otp_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='XDRRi5']/div")))
    # Pause test execution to take OTP input from user
    print("Waiting for OTP input...")
    time.sleep(10)  # Adjust this sleep time as needed for OTP input
    otp = input("Please enter the OTP sent to your mobile: ")
    if otp and len(otp) == 6:
        otp_fields = wait.until(EC.presence_of_all_elements_located((By.XPATH, "(//input[@class='r4vIwl IX3CMV'])")))
        for i, digit in enumerate(otp):
            otp_fields[i].send_keys(digit)
    driver.find_element(By.XPATH, "//button[contains(text(),'Verify')]").click()
    time.sleep(5)  # Wait for verification to complete

    # Wait for login to complete
    profile_icon = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@class='_1TOQfO'])[1]")))
    webdriver.ActionChains(driver).move_to_element(profile_icon).perform()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Logout']")))
    

    # Search for a product
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Select first product
    product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='_75nlfW']//a)[1]")))
    product.click()

    # Switch to new tab
    driver.switch_to.window(driver.window_handles[1])

    # Add to cart
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]")))
    add_to_cart_btn.click()

    # Go to cart
    cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Cart']")))
    cart_btn.click()

    # Wait for cart page
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Price details')]")))

    # Logout
    account_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_3ZeUN+']")))
    webdriver.ActionChains(driver).move_to_element(account_menu).perform()
    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Logout']")))
    logout_btn.click()

    # Wait for login button to reappear
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Login')]")))

    # Close the tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])