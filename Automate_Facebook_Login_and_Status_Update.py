import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# To use Google Chrome with Selenium,
# First install Google Chrome Driver from 'https://sites.google.com/a/chromium.org/chromedriver/'
# Then replace 'C:/chrome/chromedriver.exe' with your chrome driver path

# driver = webdriver.Chrome('C:/chrome/chromedriver.exe')# Uncomment to use Google Chrome Browser

driver = webdriver.Firefox()  # Firefox Browser
driver.get('http://www.facebook.com')
time.sleep(5)

# Email address and password field on facebook login
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")

# Send values for email address and password fields
username.send_keys("example@gmail.com")
password.send_keys("password123")

# Wait one second before pressing login button
time.sleep(1)

# Click the login button after entering email address and password
driver.find_element_by_id("loginbutton").click()

# Locating the text box where it says -> What's on your mind?
message = driver.find_element(By.XPATH, "//textarea[@name='xhpc_message']")

# Get the text box in focus where it says -> What's on your mind?
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(message) \
    .key_up(Keys.CONTROL) \
    .perform()

# Message for status update
message.send_keys("Ha Ha")

# Click the post button after writing the status update
driver.find_element(By.XPATH, '//button[text()="Post"]').click()
time.sleep(5)

# Close the browser
driver.close()
