from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Users/Admin/PycharmProjects/SeleniumPython/Drivers/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self
company_name_text = driver.find_element(By.XPATH, "//a[contains(text(),'eClerx Services')]/self::a").text
print(company_name_text)

# parent
company_name_text_1 = driver.find_element(By.XPATH, "//a[contains(text(),'eClerx Services')]/parent::td").text
print(company_name_text_1)

# child & ancestor
child_values = driver.find_elements(By.XPATH, "//a[contains(text(),'eClerx Services')]/ancestor::tr/child::td")
# text method can not be used with find_elements, so we can use count method to get count of elements
print(len(child_values))
# To print text of all elements:
for i in child_values:
    print(i.text)

# ancestor
ancestor_values = driver.find_element(By.XPATH, "//a[contains(text(),'eClerx Services')]/ancestor::tr").text
print(ancestor_values)

# descendant & ancestor
descendant_values = driver.find_elements(By.XPATH,
                                         "//a[contains(text(),'eClerx Services')]/ancestor::tr/descendant::td")
print(len(descendant_values))
# To print text of all elements:
for j in descendant_values:
    print(j.text)

# following
following_elements = driver.find_elements(By.XPATH, "//a[contains(text(),'eClerx Services')]/following::td")
print(len(following_elements))

# following-sibling
following_sibling = driver.find_elements(By.XPATH, "//a[contains(text(),'eClerx "
                                                   "Services')]/ancestor::tr/following-sibling::tr")
print(len(following_sibling))

# preceding
preceding_elements = driver.find_elements(By.XPATH,
                                          "//a[contains(text(),'eClerx Services')]/ancestor::tr/preceding::tr")
print(len(preceding_elements))

# preceding_sibling
preceding_sibling = driver.find_elements(By.XPATH, "//a[contains(text(),'eClerx "
                                                   "Services')]/ancestor::tr/preceding-sibling::tr")
print(len(preceding_sibling))
