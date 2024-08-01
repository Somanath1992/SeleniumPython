from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
# How to Add new cookie
driver.add_cookie({'name': 'somanath', 'value': '1234'})

# Capture Cookies from the browser
cookies = driver.get_cookies()  # its dictionary object , data is stored in key and value pair
print("size of cookies:", len(cookies))

# Print details of all cookies
for cookie in cookies:
    print(cookie)
    # To get specific value
    print(cookie.get('name'), ":", cookie.get('value'))

# Delete specific cookie from the browser
driver.delete_cookie("somanath")
cookies = driver.get_cookies()
print("size of cookies:", len(cookies))

# Delete All cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of cookies:", len(cookies))
