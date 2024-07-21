import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")
min_slider_post = driver.find_element(By.XPATH, "//span[contains(@class,'ui-slider-handle')][1]")
max_slider_post = driver.find_element(By.XPATH, "//span[contains(@class,'ui-slider-handle')][2]")

print("Location Before Sliding")
print(min_slider_post.location)
print(max_slider_post.location)

action = ActionChains(driver)
action.drag_and_drop_by_offset(min_slider_post, 100, 0).perform()
action.drag_and_drop_by_offset(max_slider_post, -39, 0).perform()

print("Location After Sliding")
print(min_slider_post.location)
print(max_slider_post.location)

time.sleep(3)
