#import selenium
from  selenium import webdriver
#from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys

options = Options()
options.binary_location="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

driver_path = "C:\\Users\\UMUT\\Downloads\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
browser.get("https://twitter.com")
time.sleep(2)

browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div').click()
time.sleep(2)
# fill the number or mail
browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys('knay_umut')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div').click()
time.sleep(2)
# fill the password
browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys('Qwert123.')
 
# clicking on that element 
time.sleep(2)
browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
time.sleep(2)
browser.get("https://twitter.com/knay_umut")