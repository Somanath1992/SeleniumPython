import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(3)
login = driver.find_element(By.XPATH, "(//a[@title='Login'])[1]")
wishlist = driver.find_element(By.XPATH, "//li[text()='Wishlist']")
time.sleep(2)
action = ActionChains(driver)
action.move_to_element(login).move_to_element(wishlist).click().perform()
time.sleep(2)
