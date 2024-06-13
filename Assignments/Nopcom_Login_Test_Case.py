"""Test Case:
1.Open Web Browser (Chrome/Firefox/Edge)
2.Open URL https://admin-demo.nopcommerce.com/login
3.Enter Username (admin@yourstore.com)
4.Enter Password (admin)
5.Click on Login
6.Compare title of the home page (Actual title)
7.Verify title of the page: Dashboard / nopCommerce administration (Expected)
8.Close Browser
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='Email']").clear()
driver.find_element(By.XPATH, "//input[@name='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH, "//input[@name='Password']").clear()
driver.find_element(By.XPATH, "//input[@name='Password']").send_keys("admin")
driver.find_element(By.XPATH, "//button[text()='Log in']").click()
act_page_title = driver.title
exp_page_title = "Dashboard / nopCommerce administration"

# verify page title
if act_page_title == exp_page_title:
    print("Actual and Expected Page titles are same,Login Test Passed and Actual Page title is: " + act_page_title)
else:
    print("Actual and Expected Page titles are not same,Login Test Failed and Actual Page title is: " + act_page_title)

driver.close()
