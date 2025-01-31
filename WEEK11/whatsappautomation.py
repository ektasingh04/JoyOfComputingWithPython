'''

'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driv=webdriver.Chrome("path od webdriver") #last time this variable was named browser
driv.get("https:/web.whatsapp.com/")
wait=WebDriverWait(driv,600)

target='"tanvi"'  #friend name
string="i want to send this msg"

#locationg a msg box-- it is not in div tag but under span tag
X_arg="//span[contains(@title,'+target+')]"
target=wait.until(ec.prsence_of_element_located((By.XPATH, X_arg)))
target.click()

#send msg.. locate text box... find element by class will have msg body now
inputbox=driv.find_element_by_class_name('_1Plpp')
for i in range(50):
    inputbox.send_keys(string+Keys.ENTER)