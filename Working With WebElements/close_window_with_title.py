import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.orangehrm.com/en/book-a-free-demo/")
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Executive Profile']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Our Offices']").click()
windowIds = driver.window_handles
for winid in windowIds:
    driver.switch_to.window(winid)
    if driver.title == "Our Offices | OrangeHRM":
        driver.close()


