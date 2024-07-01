from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)  # applicable for all below statements
driver.maximize_window()
driver.get("https://www.google.com/")
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
search_box.send_keys("selenium")
search_box.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']//parent::a[@href='https://www.selenium.dev/']").click()
