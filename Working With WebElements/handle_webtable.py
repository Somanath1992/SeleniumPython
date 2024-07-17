# 1. Count Number of rows and columns
# 2. Read Specific row and columns
# 3. Read all rows and columns
# 4. Read data based on condition
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
# Print total number of rows
total_rows = len(rows)
print(total_rows)
cols = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
# Print total number of columns
total_cols = len(cols)
print(total_cols)
# Read Specific row and columns
book_name_ele = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]")
print(book_name_ele.text)

# Read All rows and columns data
for row in range(2, total_rows + 1):
    for col in range(1, total_cols + 1):
        # Replacing x path with dynamic row and column
        data = driver.find_element(By.XPATH,
                                   "//table[@name='BookTable']//tr[" + str(row) + "]/td[" + str(col) + "]").text
        print(data, end='   ')
    print()

# Read data based on condition [print book name whose auther is mukesh]
for row in range(2, total_rows + 1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[2]").text
    if author_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[1]").text
        print(book_name, " ", author_name)
