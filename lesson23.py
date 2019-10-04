# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:16:31 2019

@author: sokol
"""

import sys
import math
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def func(num):
    return str(math.log(abs(12*math.sin(int(num)))))


def script23_0(browser):
    pass


def script23_1(browser):
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    browser.find_element_by_class_name('btn-primary').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    num = int(browser.find_element_by_css_selector('span#input_value').text)
    browser.find_element_by_css_selector('input#answer').send_keys(func(num))

    #насладиться результатом
    time.sleep(1)

    browser.find_element_by_css_selector('button.btn-primary').click()


def script23_2(browser):
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element_by_class_name('btn-primary').click()

    windows = browser.window_handles
    browser.switch_to.window(windows[-1])

    num = int(browser.find_element_by_css_selector('span#input_value').text)
    browser.find_element_by_css_selector('input#answer').send_keys(func(num))

    #насладиться результатом
    time.sleep(1)

    browser.find_element_by_css_selector('button.btn-primary').click()


def script24_0(browser):
    link = "http://suninjuly.github.io/wait1.html"
    link = "http://suninjuly.github.io/wait2.html"
    browser.get(link)

    #time.sleep(1)
    browser.find_element_by_id('verify').click()

    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text


def script24_1(browser):
    link = "http://suninjuly.github.io/wait1.html"
    link = "http://suninjuly.github.io/wait2.html"
    browser.get(link)

    button = WebDriverWait(browser,5).until(\
                          EC.element_to_be_clickable((By.ID,"verify")))
    button.click()

    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

def script24_2(browser):
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    #element = browser.find_element_by_css_selector("div.card-body div #price")

    WebDriverWait(browser,12).until(
                          EC.text_to_be_present_in_element (
        (By.CSS_SELECTOR,"div.card-body div #price"),"$100"))
    browser.find_element_by_css_selector("button#book").click()

    #find next x
    num = browser.find_element_by_css_selector("span#input_value").text
    browser.find_element_by_css_selector("input#answer").send_keys(func(num))
    button = browser.find_element_by_css_selector("button#solve")

    #насладиться результатом
    #time.sleep(0.5)

    button.click()


if __name__ == "__main__":

    try:
        brs = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
        brs.implicitly_wait(5)
        if len(sys.argv)>1:
            arg1 = sys.argv[1]
        else:
            arg1 = '0'

        if arg1 == '1':
            script23_1(brs)
        elif arg1 == '2':
            script23_2(brs)
        elif arg1 == '40':
            script24_0(brs)
        elif arg1 == '41':
            script24_1(brs)
        elif arg1 == '42':
            script24_2(brs)
        else:
            script23_0(brs)

    finally:
        print('...driver has stopped normally')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        brs.quit()