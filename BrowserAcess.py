from robobrowser import RoboBrowser
from selenium import webdriver as web
browser = RoboBrowser()
login_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfp02Bl3Ne09pPMjmAEvY85APA2zHzRlIA9TbUJmA2fQR4how/viewform'
browser.open(login_url)
form = browser.get_form(id='mG61Hd')

import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)

for i in data:
    Fname = i[0]
    Lname = i[1]
    Rnumb = i[2]
    last = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    last.send_keys(Fname)
    last = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    last.send_keys(Lname)
    last = web.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    last.send_keys(Rnumb)
    Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    Submit.click()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfp02Bl3Ne09pPMjmAEvY85APA2zHzRlIA9TbUJmA2fQR4how/viewform')

browser.submit_form(form)
