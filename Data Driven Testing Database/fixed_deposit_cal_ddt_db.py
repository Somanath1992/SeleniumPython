import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import mysql.connector

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI"
           "-BSB001.html")
try:
    connc = mysql.connector.connect(host="localhost", port="3306", username="root", password="9423", database="sakila")
    curs = connc.cursor()
    curs.execute("select * from caldata")
    # To print records from the table
    for row in curs:
        # Reading data from database
        principle = row[0]
        roi = row[1]
        period1 = row[2]
        period2 = row[3]
        freq = row[4]
        exp_maturity = row[5]

        # Passing data to the application
        driver.find_element(By.XPATH, "//input[@name='principal']").send_keys(principle)
        driver.find_element(By.XPATH, "//input[@name='interest']").send_keys(roi)
        driver.find_element(By.XPATH, "//input[@name='tenure']").send_keys(period1)
        period_drp_dwn = Select(driver.find_element(By.XPATH, "//select[@name='tenurePeriod']"))
        period_drp_dwn.select_by_visible_text(period2)
        freq_drp_dwn = Select(driver.find_element(By.XPATH, "//select[@name='frequency']"))
        freq_drp_dwn.select_by_visible_text(freq)
        driver.find_element(By.XPATH, "//div[@class='CTR PT15']/a[1]").click()
        act_maturity = driver.find_element(By.XPATH, "//span[@name='resp_matval']").text

        # Validation
        if float(exp_maturity) == float(act_maturity):
            print("Test Passed")

        else:
            print("Test Failed")

        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@class='PL5']").click()
    connc.close()
except:
    print("Connection Error")
driver.close()
