import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
# Find Number of Links on a Page
links = driver.find_elements(By.TAG_NAME, 'a')
print("total number of links", len(links))

# Print All Link Names
for link in links:
    print(link.text)
