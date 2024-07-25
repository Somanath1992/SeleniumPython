import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://text-compare.com/")
input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")
input1.send_keys("welcome to selenium")
time.sleep(2)
action = ActionChains(driver)

# To select text from input1 box -> CTRL+A
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# To Copy Text -> CTRL+C
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# To shift focus to input2 box -> TAB
action.send_keys(Keys.TAB).perform()

# To paste text into input2 box -> CTRL+V
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(2)
