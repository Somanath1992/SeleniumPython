import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
double_click_btn = driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
action = ActionChains(driver)
action.double_click(double_click_btn).perform()
time.sleep(3)
print(driver.switch_to.alert.text)
