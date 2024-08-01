from selenium import webdriver


def headless_chrome_setup():
    from selenium.webdriver.chrome.service import Service
    chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver


def headless_edge_setup():
    from selenium.webdriver.edge.service import Service
    edge_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/msedgedriver.exe"
    service = Service(edge_driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driver = webdriver.Edge(service=service, options=options)
    return driver


def headless_firefox_setup():
    from selenium.webdriver.firefox.service import Service
    firefox_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/geckodriver.exe"
    service = Service(firefox_driver_path)
    options = webdriver.FirefoxOptions()
    # options.headless = True
    options.add_argument("--headless")
    options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
    driver = webdriver.Firefox(service=service, options=options)
    return driver


driver = headless_chrome_setup()
driver = headless_edge_setup()
driver = headless_firefox_setup()
driver.get("https://demo.nopcommerce.com/")
print(driver.current_url, " ", driver.title)
