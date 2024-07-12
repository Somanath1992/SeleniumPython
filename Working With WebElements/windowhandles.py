import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
# To open chrome open after code execution , because it is closing automatically without sending any command
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.orangehrm.com/en/book-a-free-demo/")
# To Get Current window id
windowId = driver.current_window_handle
print(windowId)
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM']").click()
windowIds = driver.window_handles
# Approach 1:
parent_win_id = windowIds[0]
child_win_id = windowIds[1]
print(parent_win_id, child_win_id)
driver.switch_to.window(child_win_id)
print("Title of child window is:", driver.title)
driver.switch_to.window(parent_win_id)
print("Title of parent window is:", driver.title)

# Approach 2: Using for loop
for winid in windowIds:
    driver.switch_to.window(winid)
    print(driver.title)
driver.quit()

