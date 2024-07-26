import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
time.sleep(3)
country_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(country_list))
for country in country_list:
    if country.text == "Australia":
        country.click()
        break

time.sleep(3)
