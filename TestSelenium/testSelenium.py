from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = r"C:\chromedriver\chromedriver.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

service = Service(driver_path)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://python.org")
driver.close()