# To get the response code of link, we need to install requests package from interpreter setting
import time
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")
links = driver.find_elements(By.TAG_NAME, 'a')
count = 0
for link in links:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, " is valid link")
print("total number of broken link", count)
