# To handle dropdown we have select class in selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
# driver.get("https://www.opencart.com/index.php?route=account/register")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
dropdown = driver.find_element(By.XPATH, "//select[@name='DateOfBirthMonth']")
dropdown_ele = Select(dropdown)

# Select option from dropdown
dropdown_ele.select_by_visible_text("January")
time.sleep(2)
# Value is attribute of element in DOM
dropdown_ele.select_by_value("10")  # Argentina
time.sleep(2)
# index we have to count manually and it starts from 0
dropdown_ele.select_by_index(10)
time.sleep(2)

# Capture All Options and Print Them
options_in_drp = dropdown_ele.options
print("total number of options", len(options_in_drp))
for opt in options_in_drp:
    print(opt.text)

# Select option from dropdown without using built-in functions (interview question)
for opt in options_in_drp:
    if opt.text == "July":
        opt.click()
        break

