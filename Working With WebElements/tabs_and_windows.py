import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

# Selenium 3: It opens in new tab but driver focus is on first tab only
reg_link_in_new_tab = Keys.CONTROL + Keys.RETURN    # This will perform ctrl+click/enter
driver.find_element(By.XPATH, "//a[text()='Register']").send_keys(reg_link_in_new_tab)
time.sleep(3)

# Selenium 4: Open new tab and focus on it instead of first
# Open two different urls in two different tabs and focus on latest launched tab/url
driver.get("https://www.opencart.com/")
# To launch new url in another tab
driver.switch_to.new_window("tab")
driver.get("https://www.flipkart.com/")
time.sleep(3)

# Open in new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")
driver.get("https://www.flipkart.com/")
time.sleep(3)
