from selenium import webdriver 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import getpass
from argparse import ArgumentParser
from time import sleep
import sys
# for cross compatibility with python 2/3
if sys.version[0] == '3': raw_input=input 

class Blocker():
    def __init__(self, username, password, wait=2):
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
        self.wait = wait
    
    def quit(self):
        self.driver.quit()
        
    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(3)
        username_el = self.driver.find_element("name", "username")
        password_el = self.driver.find_element("name", "password")
        username_el.send_keys(self.username)
        password_el.send_keys(self.password)
        password_el.submit()
        
        # Wait for the page to load after login
        time.sleep(self.wait)

        nn_btn = self.driver.find_element(By.CLASS_NAME, "x1yc6y37")
        nn_text_val = nn_btn.text
    
        if nn_text_val == 'Not now':
            print('nn btn present')
            nn_btn.click()

        
        print('should be logged in')

if __name__ == '__main__':
    from argparse import ArgumentParser
    import getpass
    import time
    
    parser = ArgumentParser(description='Block everyone on the blocklist on your Instagram. Requires Firefox')
    parser.add_argument('--wait', type=float, default=1, help="Explicit wait time between page loads (default 2 seconds)")
    args = parser.parse_args()
    
    username = input("Please enter your Instagram username: ")
    password = getpass.getpass('Please enter your Instagram password: ')
    blocker = Blocker(username=username, password=password, wait=args.wait)
    blocker.login()