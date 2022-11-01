from linkedin_scraper import Person, actions
from selenium import webdriver
import chromedriver_autoinstaller
import json

#STILL IN PROGRESS

driver = webdriver.Chrome("chromedriver.exe")

jobTitle = 'hr'

f = open('my_linkedin_username_password.json', 'r')
login = json.load(f)
f.close()

print(login.get())

email = login.keys()[0]
password = login.get
print(driver.find_element_by_id(email))
actions.login(driver, email, password)
person = Person(job_title = jobTitle, driver = driver)

print(person)