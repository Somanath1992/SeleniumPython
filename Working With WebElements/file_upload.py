import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
driver.find_element(By.XPATH, "//input[@name='userfile']").send_keys("C:/Users/Admin/Downloads/file-sample_100kB.doc")
time.sleep(3)
