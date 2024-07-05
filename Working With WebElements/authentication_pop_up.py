from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.implicitly_wait(10)
# To verify Login is Successful
landing_page_text = driver.find_element(By.XPATH, "//div[@class='example']")
print(landing_page_text.text)
