import selenium
from  selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

driver_path = "C:\\Users\\UMUT\\Downloads\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
browser.get("https://www.twitter.com/")
