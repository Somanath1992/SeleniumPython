import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def handle_checkbox_by_passing_args(choice):
    chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    # Scenario 1: To handle only one checkbox
    # search_box = driver.find_element(By.XPATH, "//input[@id='sunday']")
    # chk_state = search_box.is_selected()
    # if choice == 'yes' and not chk_state:
    #    search_box.click()
    # elif choice == 'no' and chk_state:
    #    search_box.click()

    # Scenario 2: To handle all checkboxes
    day_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
    for checkbox in day_checkboxes:
        chk_state = checkbox.is_selected()
        if choice == 'yes' and not chk_state:
            checkbox.click()
        elif choice == 'no' and chk_state:
            checkbox.click()


time.sleep(10)
handle_checkbox_by_passing_args('yes')
handle_checkbox_by_passing_args('no')
