from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome('./webdriver/chromedriver', options=c)
driver.get("https://ma.equatorialenergia.com.br/")
assert "Equatorial Energia – MA" in driver.title

elem = driver.find_element(By.NAME, "conta-contrato")
elem.clear()
elem.send_keys("38146327")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
try:
    element = WebDriverWait(driver, 800).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="list-bills"]/tr/td[2]'))
    )
    value = driver.find_element(By.XPATH, '//*[@id="list-bills"]/tr/td[2]').text
    print(value)
    expirationDate = driver.find_element(By.XPATH, '//*[@id="list-bills"]/tr/td[3]').text
    print(expirationDate)
    table = driver.find_element(By.XPATH,'//*[@id="list-bills"]').text
    print(table)
finally:
    driver.delete_all_cookies()
    driver.quit()