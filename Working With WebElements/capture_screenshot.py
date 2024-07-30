from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.save_screenshot(os.getcwd()+"/google.png")
driver.get_screenshot_as_file(os.getcwd()+"/google1.png")
# driver.get_screenshot_as_png() - Saves screenshot in binary format
# driver.get_screenshot_as_base64() - Saves screenshot in binary format
