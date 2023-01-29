import os
from selenium import webdriver

os.environ['PATH'] += "c:\Selenium_Driver"
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com")
# nakon pokretanja dobivamo poruku Chrome is being controlled by automated test software
driver.implicitly_wait(30)
my_element = driver.find_element()#ostavljeno namjerno da se pojavi greška jer omogućuje da se chrome ne isključi odmah. Jer ako nema greške webdriver se isključuje i zatvara browser.
my_element.click()
