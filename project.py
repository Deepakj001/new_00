from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_facebook(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.facebook.com/")  # Open the Facebook login page

    # Find the username (email or phone) and password input fields
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(EC.url_contains("facebook.com"))  # Wait for the login process to complete

    return driver

def check_new_messages(driver):
    driver.get("https://www.facebook.com/messages/")  # Navigate to the Facebook messages page

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Conversations']")))

    new_messages = driver.find_elements(By.XPATH, "//div[@aria-label='Conversations']//div[contains(@class, 'unread')]")
    if new_messages:
        print(f"You have {len(new_messages)} new messages:")
        for message in new_messages:
            print(message.text)
    else:
        print("No new messages.")

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with actual login credentials
    username = "/"
    password = "/"

    driver = login_to_facebook(username, password)

    if driver:
        check_new_messages(driver)

    # Take a screenshot for debugging purposes
    driver.save_screenshot("screenshot.png")

    # Close the browser
    driver.quit()
