import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(2)
right_click_btn = driver.find_element(By.XPATH, "//span[text()='right click me']")
action = ActionChains(driver)
# to right-click on button
action.context_click(right_click_btn).perform()
time.sleep(2)
# Click on Edit button from right click menu
driver.find_element(By.XPATH, "//span[text()='Edit']").click()
time.sleep(2)
