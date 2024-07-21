import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("C://Users/Admin/PycharmProjects/SeleniumPython/Sample Html/scrollbar.html")

# 1.Horizontal scroll using pixels
driver.execute_script("window.scrollBy(500,0)", "")
pixel_value = driver.execute_script("return window.pageXOffset;")
print("Number of pixels moved:", pixel_value)
time.sleep(3)

# 2.Horizontal Scroll to End
driver.execute_script("window.scrollBy(document.body.scrollWidth,0)")
pixel_value = driver.execute_script("return window.pageXOffset;")
print("Number of pixels moved:", pixel_value)
time.sleep(3)

# 3.Horizontal scroll at extreme left end
driver.execute_script("window.scrollBy(-document.body.scrollWidth,0)")
pixel_value = driver.execute_script("return window.pageXOffset;")
print("Number of pixels moved:", pixel_value)
time.sleep(3)

# 4.Horizontal Scroll based on element visibility
fifth_ele = driver.find_element(By.XPATH, "//div[text()='Item 5']")
driver.execute_script("arguments[0].scrollIntoView();", fifth_ele)
pixel_value = driver.execute_script("return window.pageXOffset;")
print("Number of pixels moved:", pixel_value)
time.sleep(3)
