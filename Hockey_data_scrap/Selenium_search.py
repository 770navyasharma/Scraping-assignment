'''For implementing the searching mechanism we can use selenium and webdriver to perform serch by input of the user and diltering down the contents then performing further operations on them like saving to postgre or analysis.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://www.scrapethissite.com/pages/forms/")
print(driver.title)

search = driver.find_element(By.NAME, "q")
search.send_keys("Calgary Flames") #Team name(here, "Calgary Flames") can be a user input.
search.send_keys(Keys.RETURN)

try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table"))
    )
    # header = table.find_elements(By.TAG_NAME, 'th')
    # for h in header:
    #     print(h.text)
    
finally:
    driver.quit()