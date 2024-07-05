import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# Opens Alert Window
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(3)
alert_window = driver.switch_to.alert
print(alert_window.text)
time.sleep(2)
alert_window.send_keys("Test")
time.sleep(2)
# CLick OK Button
alert_window.accept()
time.sleep(2)
# Click on Cancel Button
# alert_window.dismiss()
# Capture Text Entered in on POP Up from Result Section
print(driver.find_element(By.XPATH, "//p[@id='result']").text)
