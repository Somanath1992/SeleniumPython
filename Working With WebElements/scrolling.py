import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.duxburysystems.com/documentation/dbt12.7/Content/samples/word/samples.htm")
time.sleep(5)
# 1. Scroll down page by pixel
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
pixel_value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", pixel_value)

# 2.Scroll down page based on element visibility
marathi_lang = driver.find_element(By.XPATH, "//a[text()='Marathi']")
driver.execute_script("arguments[0].scrollIntoView();", marathi_lang)
pixel_scrolled = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", pixel_scrolled)
time.sleep(3)

# 3.Scroll down to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
pixel_at_end = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", pixel_at_end)

# 4.Scroll up at top of the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
pixel_at_top = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", pixel_at_top)
time.sleep(3)

