# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:34:05 2019

@author: sokol
"""

import math
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
    
def script_21_0(browser):
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    num = browser.find_element_by_css_selector("span#input_value").text
    
    element = browser.find_element_by_css_selector("input#answer")
    element.send_keys( calc(num) )
    
    element = browser.find_element_by_css_selector("input#robotCheckbox")
    element.click()
    
    element = browser.find_element_by_css_selector("input#robotsRule")
    element.click()
    
    #насладиться результатом
    time.sleep(3)
    
    element = browser.find_element_by_css_selector("button.btn-default")
    element.click()
    
    
def script_21_1(browser):
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    element = browser.find_element_by_css_selector("img#treasure")
    num = element.get_attribute('valuex')
    
    element = browser.find_element_by_css_selector("input#answer")
    element.send_keys( calc(num) )
    
    element = browser.find_element_by_css_selector("input#robotCheckbox")
    element.click()
    
    element = browser.find_element_by_css_selector("input#robotsRule")
    element.click()
    
    #насладиться результатом
    time.sleep(3)
    
    element = browser.find_element_by_css_selector("button.btn-default")
    element.click()


def script_21_2(browser):
    
    
    link1 = "http://suninjuly.github.io/selects1.html"
    link2 = "http://suninjuly.github.io/selects2.html"
    browser.get(link2)

    summa = int(browser.find_element_by_css_selector("span.nowrap#num1").text) + \
            int(browser.find_element_by_css_selector("span.nowrap#num2").text)                                         
   
    selector = Select( browser.find_element_by_css_selector("select#dropdown.custom-select") )
    selector.select_by_value(str(summa))
    
    #насладиться результатом
    time.sleep(3)
    
    element = browser.find_element_by_css_selector("button.btn-default")
    element.click()


def script_21_3(browser):
    
    
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    num = browser.find_element_by_css_selector("span#input_value").text
   
    element = browser.find_element_by_css_selector("input#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.send_keys( calc(num) )
    
    element = browser.find_element_by_css_selector("input#robotCheckbox")
    element.click()
    
    element = browser.find_element_by_css_selector("input#robotsRule")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()
    
    
    #насладиться результатом
    time.sleep(1)
    
    element = browser.find_element_by_css_selector("button.btn-primary")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()    

def script_21_4(browser):
    print( os.path.abspath(__file__))
    print( os.path.abspath(os.path.dirname(__file__)))
    print( os.path.abspath(os.path.dirname(__file__))+'\\new_file.py')
    
    link ="http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    browser.find_element_by_css_selector("input[name='firstname']").send_keys("Andrei")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("Sokolov")
    browser.find_element_by_css_selector("input[name='email']").send_keys("name_surname@mail.ru")
    
    file_name = os.path.dirname(os.path.abspath(__file__))+'\\new_file.txt'
    browser.find_element_by_css_selector("input[name='file']").send_keys(file_name)
    
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
    
    
if __name__ == '__main__':
    
    try:
        browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
        if len(sys.argv) > 1:
            arg = sys.argv[1:]
        else:
            arg=['0']
        
        if arg[0] == '1':
            script_21_1(browser)
        elif arg[0] == '2':
            script_21_2(browser)
        elif arg[0] == '3':
            script_21_3(browser)
        elif arg[0] == '4':
            script_21_4(browser)
        else:
            script_21_0(browser)
        
    finally:    
        print('Driver is stopped normally')
        time.sleep(15)
        browser.quit()
        
