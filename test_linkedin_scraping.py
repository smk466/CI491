from selenium import webdriver

# open linkedin
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.linkedin.com')

#username = driver.find_element