import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH, "//input[@name='dob']").click()
month = driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']")
month_drpdwn = Select(month)
month_drpdwn.select_by_visible_text("Apr")
year = driver.find_element(By.XPATH, "//select[@data-handler='selectYear']")
year_drpdwn = Select(year)
year_drpdwn.select_by_visible_text("1992")
dates = driver.find_elements(By.XPATH, "//td[@data-handler='selectDay']")
for date in dates:
    if date.text == "27":
        date.click()
        break
time.sleep(2)
