# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:04:24 2018

@author: Clif
"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import psutil

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

username_field = driver.find_element_by_id("username")
username_field.send_keys(username)
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)


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


#select the rank button
# for i in range(1, (len(rows)-1)):
    #open in new tab
    # posting = driver.find_element_by_css_selector(("#search-results-table "+
    #                                                "> tbody "+
    #                                                "> tr:nth-child("+str(i)+
    #                                                ") "+
    #                                                "> td:nth-child(4) > a"))
    # actions.key_down(Keys.CONTROL).click(posting).key_up(Keys.CONTROL).perform()

    #switch to new tab
