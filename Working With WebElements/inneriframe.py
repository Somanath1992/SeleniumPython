import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']").click()
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)
# Switch to inner frame
inner_frame = driver.find_element(By.XPATH, "//h5[text()='Nested iFrames']/following::iframe")
driver.switch_to.frame(inner_frame)
# Enter text in inner frame's text box
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")
time.sleep(2)
# Navigating back to parent frame
driver.switch_to.parent_frame()     # Outer iframe

