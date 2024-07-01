from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# myWait = WebDriverWait(driver, 10)  # Basic Syntax
# advance syntax we can handle exceptions, check element after certain ferquncy
myWait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[Exception])
driver.get("https://www.google.com/")
search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
search_box.send_keys("selenium")
search_box.submit()
# implementation of explicit wait
search_link = myWait.until(ec.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']//parent::a["
                                                                     "@href='https://www.selenium.dev/']")))

search_link.click()
