import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(2)
source = driver.find_element(By.XPATH, "(//div[text()='Washington'])[2]")
target = driver.find_element(By.XPATH, "//div[text()='United States']")
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
time.sleep(3)
