import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import excel_utils

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI"
           "-BSB001.html")

excel_file_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Data Driven Testing/Test Excel Files/caldata.xlsx"

rows = excel_utils.get_row_count(excel_file_path, 'Sheet1')
for row in range(2, rows + 1):
    # Reading data from excel
    principle = excel_utils.read_data(excel_file_path, 'Sheet1', row, 1)
    roi = excel_utils.read_data(excel_file_path, 'Sheet1', row, 2)
    period1 = excel_utils.read_data(excel_file_path, 'Sheet1', row, 3)
    period2 = excel_utils.read_data(excel_file_path, 'Sheet1', row, 4)
    freq = excel_utils.read_data(excel_file_path, 'Sheet1', row, 5)
    exp_maturity = excel_utils.read_data(excel_file_path, 'Sheet1', row, 6)

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
        excel_utils.write_data(excel_file_path, "Sheet1", row, 8, "Pass")
        excel_utils.fill_green_color(excel_file_path, "Sheet1", row, 8)
    else:
        print("Test Failed")
        excel_utils.write_data(excel_file_path, "Sheet1", row, 8, "Fail")
        excel_utils.fill_red_color(excel_file_path, "Sheet1", row, 8)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@class='PL5']").click()
driver.close()
