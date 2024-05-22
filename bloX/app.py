from block_list import to_be_blocked
from selenium import webdriver
from selenium.webdriver.common.by import By 
import getpass
from argparse import ArgumentParser 
from time import sleep
import sys
# for cross compatibility with python 2/3
if sys.version[0] == '3': raw_input=input

class Blocker():
    def __init__(self, username, password, wait=8, headless=False):
        if headless: 
            option = webdriver.FirefoxOptions()
            option.addd_argument("--headless")
            self.driver = webdriver.Firefox(options=option)
            print('Running in headless mode...')
        else: 
            self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
        self.wait = wait
        
    def quit(self):
        self.driver.quit()
        
    def login(self):
        pass
        