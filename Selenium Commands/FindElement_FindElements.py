import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://demo.nopcommerce.com")

# find_element() - Returns single webelement
# 1.Locator matching with single webelement
element = driver.find_element(By.XPATH, "//input[@name='q']")
element.send_keys("Apple 13 pro")

# 2.Locator matching with multiple webelements
link_element = driver.find_element(By.XPATH, "//div[@class='footer-upper']//a")
print(link_element.text)  # will print text of first webelement

# 3.Element not available then throw NoSuchElementException
# driver.find_element(By.XPATH,"//a[text()='Log i']").click()

# find_elements() - Returns multiple webelements
# 1.Locator matching with single webelement
elements = driver.find_elements(By.XPATH, "//input[@name='q']")
print(len(elements))
elements[0].send_keys("Apple")

# 2.Locator matching with multiple webelements
link_elements = driver.find_elements(By.XPATH, "//div[@class='footer-upper']//a")
print(len(link_elements))
for i in link_elements:
    print(i.text)

# 3.Element not available
login_element = driver.find_elements(By.XPATH, "//a[text()='Log i']")
print(len(login_element))
