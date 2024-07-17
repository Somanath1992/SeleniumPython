import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
# Using SendKeys method
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("07/16/2024")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

year = "2025"
month = "July"
date = "16"

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//a[@title='Next']").click()
        # driver.find_element(By.XPATH,"//a[@title='Prev']").click() - previous arrow for past dates
dates = driver.find_elements(By.XPATH, "//a[contains(@class,'ui-state')]")
for day in dates:
    if day.text == date:
        day.click()
        break
time.sleep(2)
