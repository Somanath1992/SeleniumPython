import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
# Navigate/Focus on the Frame
driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
time.sleep(2)
# to switch focus from frame to main page
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//label[text()='Male']").click()
time.sleep(2)
