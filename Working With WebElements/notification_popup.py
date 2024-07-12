from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# To disable browser based notification pop-ups like location or want to send notification etc.
options.add_argument("--disable-notifications")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.lokmat.com/")
driver.maximize_window()
driver.close()
