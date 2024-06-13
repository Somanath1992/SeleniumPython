"""Test Case:
1.Open Web Browser (Chrome/Firefox/Edge)
2.Open URL https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
3.Enter Username (Admin)
4.Enter Password (admin123)
5.Click on Login
6.Compare title of the home page (Actual title)
7.Verify title of the page: OrangeHRM (Expected)
8.Close Browser
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.set_page_load_timeout(20)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
time.sleep(2)

act_page_title = driver.title
exp_page_title = "OrangeHRM"

# Page title Validation
if act_page_title == exp_page_title:
    print("Actual and Expected page titles are same, Login Test Passed and Page title is:" + act_page_title)
else:
    print("Actual and Expected page titles are not same, Login Test Failed and Page title is:" + act_page_title)

driver.close()
