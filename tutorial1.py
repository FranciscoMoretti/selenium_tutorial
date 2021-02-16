# Install Selenium
# Download Chorme web driver https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Users\\Francisco\\Code\\selenium-tutorial\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=PATH)

driver.get('https://www.grupogamma.com/')
print(driver.title)

search_btn = driver.find_element_by_class_name("fa-search")
search_btn.click()
try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))
    )
    search.send_keys("test")
    search.send_keys(Keys.RETURN)
except:
    driver.quit()

driver.quit()
