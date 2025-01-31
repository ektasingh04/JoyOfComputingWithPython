'''
#broswer automation library-- selenium
separate web drivers for separate browsers-- install web driver for chrome

'''
from selenium import webdriver
#initialise ur webdriver to open ur brwoser
browser=webdriver.Chrome("path of chrome driver")
#to open website on ur browser
browser.get("https:/www.seleniumhq.org")

elem=browser.find_element_by_link_text('Download') #to open a specific element of page.. allot it to a variable and click
elem.click()

#to write in search bar-- inspect the website and  find the id of search bar in header ..allot to a variable andsendkeys 
search=browser.find_element_by_id('q') 
search.send_keys('Download') #this will write in search box
