import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



os.environ['PATH'] += "c:\Selenium_Driver"
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
# nakon pokretanja dobivamo poruku Chrome is being controlled by automated test software
driver.implicitly_wait(30)
my_element = driver.find_element(By.ID, "downloadButton")#desni klik na gumb, provjeri kod, naziv button id-a
my_element.click() #automatski klik na gumb Start Download



progress_element = driver.find_element(By.ID, "")#namjerno ostavljena greška jer driver zatvara browser, nisam nasao rjesenje, nema ni na forumima
my_element.click()
