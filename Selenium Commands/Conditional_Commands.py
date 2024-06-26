import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
# is_displayed() & is_enabled()
search_box_ele = driver.find_element(By.XPATH, "//input[@name='q']")
print("Display status:", search_box_ele.is_displayed())
print("Enable status:", search_box_ele.is_enabled())

# is_selected()
male_radio_btn = driver.find_element(By.XPATH, "//input[@id='gender-male']")
female_radio_btn = driver.find_element(By.XPATH, "//input[@id='gender-female']")
# default status
print(male_radio_btn.is_selected())
print(female_radio_btn.is_selected())

male_radio_btn.click()  # select male radio button
time.sleep(2)
# after selecting male radio button
print(male_radio_btn.is_selected())
print(female_radio_btn.is_selected())

female_radio_btn.click()  # select female radio button
time.sleep(2)
# after selecting female radio button
print(male_radio_btn.is_selected())
print(female_radio_btn.is_selected())