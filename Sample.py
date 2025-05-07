from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://10.10.99.18:8002/login")
driver.maximize_window()
driver.implicitly_wait(20)

wait = WebDriverWait(driver, 20)

try:
    print("Logging in...")
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")

    username.clear()
    username.send_keys("Superadmin@gmail.com")

    password.clear()
    password.send_keys("Dost@123")
    password.send_keys(Keys.RETURN)


    assert wait.until(EC.url_contains("/dashboard"))
    print("Login successful!")

    print("Navigating to Audit page...")
    driver.get("http://10.10.99.18:8002/audit")

    print("Adding new audit entry...")
    add_icon_colored = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fas fa-plus text-white-100']")))
    add_icon_colored.click()


    print("Saving audit entry...")
    save_button = wait.until(EC.element_to_be_clickable((By.ID, "addAudit")))
    save_button.click()


    print("Audit entry saved successfully!")

    import traceback

    try:

        raise ValueError("This is a test error")
    except ValueError as e:

        print(f"An error occurred: {e}")
        # Log the error
        with open("error.log", "a") as f:
            f.write(f"Error: {e}\n")
            traceback.print_exc(file=f)

        print("Please try again later.")

    time.sleep(30)

finally:
    driver.quit()

assert save_button, "Save Successfully"