from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://admin-demo.nopcommerce.com/login")
email_box = driver.find_element(By.XPATH, "//input[@id='Email']")
email_box.clear()
email_box.send_keys("abc@gmail.com")
print("text value is :", email_box.text)  # returns nothing as there is no inner text available
print("attribute value is:", email_box.get_property('value'))
login_btn = driver.find_element(By.XPATH, "//button[text()='Log in']")
print("button text is:", login_btn.text)
print("button value attribute is:",
      login_btn.get_attribute('value'))  # returns nothing as we don't have value attribute
print("button type attribute is:", login_btn.get_attribute('type'))
