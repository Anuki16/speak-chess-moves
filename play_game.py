# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:27:48 2021

@author: Anuki Pasqual
"""

import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class last_move_has_changed(object):
    def __init__(self, locator, move):
        self.locator = locator
        self.move = move
    def __call__(self, driver):
        try: 
            element = driver.find_element(*self.locator)
        except:
            return False
        if element.text == self.move:
            return False
        return element
    
last_move_class = "move-text-selected"

def new_login():
    driver = webdriver.Chrome()
    driver.get("https://chess.com/login")
    driver.find_element_by_id("username").send_keys("milky-way")
    driver.find_element_by_id("password").send_keys("plutotim")
    driver.find_element_by_id("login").click()
    driver.get("https://chess.com/live")
    return driver
    
def new_speak_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    return engine

def speak(engine, string):
    engine.say(string)
    engine.runAndWait()
    

def speak_moves():
    global driver, engine
    last_move = ""
    wait = WebDriverWait(driver, 120)
    while True:
        last_move = wait.until(last_move_has_changed((By.CLASS_NAME, last_move_class), last_move)).text
        speak(engine, last_move)
        print(last_move)
        
    
driver = new_login()
engine = new_speak_engine()
        
        
        