# -*- coding: utf-8 -*-

""" This is a selenium script for scraping data"""
import sys
import time
import os.path
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#load the chrome driver
driver = webdriver.Chrome('C:/Users/lkirvalidze/AppData/Local/Programs/Python/chromedriver')
driver.get('http://www.xn--spezialittenliste-yqb.ch/ShowPreparations.aspx') #access website

#click the items per page selector
selectRange = driver.find_element_by_xpath('//*[@id="ctl00_cphContent_gvwPreparations_ctl13_gvwpPreparations_ddlPageSize"]')
selectRange.click()
print('clicked range selector')

#go down to 500 items
selectRange.send_keys(Keys.DOWN*5 + Keys.ENTER)
print('clicked range 500')

found = True
savePath = 'C:/Users/lkirvalidze/Documents/Python WebAutomation/extracts/'
# number of rows = 9569
row = 2
count = 1
#pageNumber = driver.find_element_by_xpath('//*[@id="ctl00_cphContent_gvwPreparations_ctl503_gvwpPreparations_txtPageNumber"]')
#pageNumber.click()
#pageNumber.send_keys(Keys.CONTROL, 'a')
#pageNumber.send_keys('14', Keys.ENTER)

while found is True:
    try:
        item = driver.find_element_by_xpath(
            '//*[@id="ctl00_cphContent_gvwPreparations"]/tbody/tr[' + str(row) + ']/td[2]/a')
        found = True
        item.click()
        item2 = driver.find_element_by_xpath(
            '//*[@id="ctl00_cphContent_gvwPreparations"]/tbody/tr[' + str(row) + ']/td[2]/a')
        # this is the content to be saved into the text file
        content = driver.find_element_by_xpath('//*[@id="ctl00_cphContent_fvwPreparation"]')
        contentStr = content.text
        # put into text file
        print('writing to file...')
        name = str(count) + '-' + str(item2.text)
        print(name)
        if name.__contains__('/'):
            name = name.replace('/', '.')

        pathName = os.path.join(savePath, name + '.txt')
        newFile = open(pathName, 'wb')
        newFile.write(contentStr.encode(sys.stdout.encoding, errors='replace'))
        newFile.close()
        row = row + 1
        count = count + 1
        print('finished writing')
    except NoSuchElementException:
        nextPage = driver.find_element_by_xpath('//*[@id="ctl00_cphContent_gvwPreparations_ctl503_gvwpPreparations_btnNext"]')
        nextPage.click()
        row = 2
        if count == 9569:
            found = False
print('process finished with ' + str(count) + ' files generated')
driver.quit()


