# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:04:24 2018

@author: Clif
"""
#TODO: make the text finding/parsing stuff into a function, get rid of nested
#ifs in that function. Hint: include panels assignment in function
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import psutil
from urllib.parse import urljoin
from re import sub, compile

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None


username = ""
password = ""
#create driver object
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=options)
actions = ActionChains(driver)

driver.get("https://webapps2.uc.edu/elce/Login")

#wait

#username_field = driver.find_element_by_id("username")
#username_field.send_keys(username)
#password_field = driver.find_element_by_id("password")
#password_field.send_keys(password)
#password_field.send_keys(Keys.RETURN)


driver.find_element_by_css_selector(".col-md-2 > a:nth-child(7)").click()
driver.find_element_by_css_selector("#viewRankMenuLink > a:nth-child(1)").click()

#actual page
#select show all
driver.find_element_by_css_selector("#search-results-table_length > label > select > option:nth-child(5)").click()

#find all of the pages we need to rank
content = driver.page_source
soup = BeautifulSoup(content, "lxml")
table = soup.find("table", id="search-results-table")
rows = table.find_all("tr", role="row")

sub_re = compile("\\n|\\xa0")
for i in range(1, (len(rows)-1)):
    href = rows[i].find("a")['href']
    url = urljoin(driver.current_url, href)
    driver.get(url)
    #wait
    soup = BeautifulSoup(driver.page_source, "lxml")
    panels = soup.find_all("div", class_="panel panel-default")
   
    for k in panels:
        #remove \n and \xa0 with sub
        #Position Name
        tag = k.find("h2")
        if tag is not None:
            if sub(sub_re, "",tag.text) == 'Rank Position':
                title = sub(sub_re,"",k.find("div", attrs={"class":"row"}).text)
        #Position Description
        tag = k.find("div", attrs={"class":"pal-label"})
        if tag is not None:
            if sub(sub_re, "",tag.text) == "Position Description":
                text = sub(sub_re, "",k.find("div", attrs={"class":"pal-content"}).text)
        #Organization Name
        tag = k.find("div", attrs={"class":"pal-label"})
        if tag is not None:
            if sub(sub_re, "",tag.text) == "Organization Name":
                author = sub(sub_re, "",k.find("div", attrs={"class":"pal-content"}).text)
    
    #grade text, author bias, ect.
    
