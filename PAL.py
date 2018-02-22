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
from postingDatabase import create_db, insert_into_db
import patternScore

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

def page_reached(driver):
    while (driver.current_url != "https://webapps2.uc.edu/elce/Student"):
        time.sleep(20)

#create driver object
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=options)
actions = ActionChains(driver)
wait = ui.WebDriverWait(driver, 10)
driver.get("https://webapps2.uc.edu/elce/Login")

#wait until body tag is found
wait.until(page_is_loaded)

#wait until login is finished. I don't want to mess with credentials more than
#neccessary.
page_reached(driver)

driver.find_element_by_css_selector(".col-md-2 > a:nth-child(7)").click()
driver.find_element_by_css_selector("#viewRankMenuLink > a:nth-child(1)").click()

wait.until(page_is_loaded)
#actual page
#select show all
driver.find_element_by_css_selector("#search-results-table_length > label > select > option:nth-child(5)").click()

#find all of the pages we need to rank
content = driver.page_source
soup = BeautifulSoup(content, "lxml")
table = soup.find("table", id="search-results-table")
rows = table.find_all("tr", role="row")
create_db()

legend = patternScore.Score_Legend()
legend.create_from_file("JobSearchRegex.txt")

eol_re = compile("\\n$")
sub_re = compile("\\n|\\xa0")
for i in range(1, (len(rows)-1)):
    href = rows[i].find("a")['href']
    url = urljoin(driver.current_url, href)
    driver.get(url)
    #wait
    wait.until(page_is_loaded)

    soup = BeautifulSoup(driver.page_source, "lxml")
    panels = soup.find_all("div", class_="panel panel-default")
    
    text = None
    title = None
    author = None
    for k in panels:
        #remove \n and \xa0 with sub
        #Position Name
        tag = k.find("h2")
        if tag is not None:
            if sub(sub_re, "",tag.text) == 'Rank Position':
                title = sub(eol_re," ",k.find("div", attrs={"class":"row"}).text)
                title = sub(sub_re, "", title)
        #Position Description
        tag = k.find("div", attrs={"class":"pal-label"})
        if tag is not None:
            if sub(sub_re, "",tag.text) == "Position Description":
                text = sub(eol_re, " ", k.find("div", attrs={"class":"pal-content"}).text)
                text = sub(sub_re, "", text)
        #Organization Name
        tag = k.find("div", attrs={"class":"pal-label"})
        if tag is not None:
            if sub(sub_re, "",tag.text) == "Organization Name":
                author = sub(eol_re, " ", k.find("div", attrs={"class":"pal-content"}).text)
                author = sub(sub_re, "", author)
    
    insert_into_db(text=text, title=title, author=author)
    #grade text, author bias, ect.
    #need to import created Scored_Legend
    doc = patternScore.Document(legend=legend, 
                                text=text, 
                                title=title, 
                                author=author)
    if doc.score_total >= 3.25:
        #apply
        
driver.close()

