import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()  # to get path of current working directory


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
    service = Service(chrome_driver_path)
    # To download file at specific location
    preferences = {"download.default_directory": location}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def edge_setup():
    from selenium.webdriver.edge.service import Service
    edge_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/msedgedriver.exe"
    service = Service(edge_driver_path)
    # To download file at specific location
    preferences = {"download.default_directory": location}
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", preferences)
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(service=service, options=options)
    return driver


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ff_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/geckodriver.exe"
    ff_binary_path = "C:/Program Files/Mozilla Firefox/firefox.exe"
    service = Service(ff_driver_path)
    options = webdriver.FirefoxOptions()
    # To download file at specific location
    options.set_preference("browser.download.folderList", 2)  # 0-Desktop,1-downloads-2-specific location
    options.set_preference("browser.download.dir", location)
    # Setting binary path as I am using Firefox ESR Version
    options.binary_location = ff_binary_path
    # To avoid save as pop up dialogue box, we need to set preference (currently it's not required)
    # options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    # options.set_preference("browser.download.manager.showWhenStarting", False)
    driver = webdriver.Firefox(service=service, options=options)
    return driver


driver = chrome_setup()
driver = edge_setup()
driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH, "(//td[@class='text-right file-link'])[1]").click()
time.sleep(10)
#driver.close()
