import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
time.sleep(2)
no_of_rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-card']"))
print("Total Number of rows are:", no_of_rows)
count = 0
for r in range(1, no_of_rows + 1):
    status = driver.find_element(By.XPATH, "//div[@class='oxd-table-card'][" + str(r) + "]/div/div[5]").text
    if status == "Disabled":
        count = count + 1

print("Number of disabled users:", count)
print("Number of enabled users:", no_of_rows - count)
