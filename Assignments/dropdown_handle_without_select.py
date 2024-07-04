import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.find_element(By.XPATH, "//select[@id='country']").click()
country_dropdown = driver.find_elements(By.XPATH, "//select[@id='country']/option")
print(len(country_dropdown))
for country_drop_down in country_dropdown:
    print(country_drop_down.text)
