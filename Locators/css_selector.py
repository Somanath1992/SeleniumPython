from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/")
driver.maximize_window()
# tag & id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# tag & class
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("xyz")
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("def")

# tag and attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_pass]").send_keys("pqr")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_pass]").send_keys("jkl")

# tag,class & attribute
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("sdf")
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("lmn")



