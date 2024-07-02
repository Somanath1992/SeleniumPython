import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
# 1.Select specific checkbox
sunday_checkbox = driver.find_element(By.XPATH, "//input[@id='sunday']")
sunday_checkbox.click()
# unchecking for further action
sunday_checkbox.click()
time.sleep(2)
# 2.Select all checkboxes
day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(day_checkboxes))
# Approach 1:
for i in range(len(day_checkboxes)):
    day_checkboxes[i].click()

# Approach 2:
for checkbox in day_checkboxes:
    checkbox.click()

# 3. Select multiple checkbox of choice
for checkbox in day_checkboxes:
    day_name = checkbox.get_attribute('value')
    if day_name == 'sunday' or day_name == 'monday':
        checkbox.click()
time.sleep(2)

# 4. Select last two checkboxes
for i in range(len(day_checkboxes) - 2, len(day_checkboxes)):
    day_checkboxes[i].click()
time.sleep(2)

# 5. Select first two checkboxes
for i in range(len(day_checkboxes)):
    if i < 2:
        day_checkboxes[i].click()
time.sleep(2)

# 6.Clear All checkboxes
for i in range(len(day_checkboxes)):
    if day_checkboxes[i].is_selected():
        day_checkboxes[i].click()
time.sleep(2)
