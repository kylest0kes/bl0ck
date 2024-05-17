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
    def __init__(self, email, password, wait=8, headless=False):
        if headless:
            option = webdriver.FirefoxOptions()
            option.add_argument("--headless")
            self.driver = webdriver.Firefox(options=option)
            print('Running in headless mode...')
        else:
            self.driver = webdriver.Firefox()
        self.email = email
        self.password = password
        self.wait = wait
    
    def quit(self):
        self.driver.quit()
        
    def login(self):
        self.driver.get('https://www.tiktok.com/login/phone-or-email/email')
        sleep(self.wait)
        email_el = self.driver.find_element(By.NAME, 'username')
        password_el = self.driver.find_element(By.CSS_SELECTOR, '.tiktok-wv3bkt-InputContainer.etcs7ny1')
        email_el.send_keys(self.email)
        password_el.send_keys(self.password)
        print('Logging in...')
        password_el.submit()
        sleep(self.wait)
        print('Logged in :)')

    def cycle_block_list(self):
        print('Beginning block cycle')
        for i in to_be_blocked:
            pass
        
    
if __name__ == '__main__':
    parser = ArgumentParser(description='Block everyone on the block_list on your Instagram. Requires Chrome')
    parser.add_argument("--wait", type=float, default=8, help="Explicit wait time between page loads (default 8 seconds to be safe)")
    parser.add_argument("--headless", action="store_true", help="Run Selenium in headless mode (hide browser window)")
    args = parser.parse_args()
    
    email = input("Please enter your TikTok email: ")
    password = getpass.getpass('Please enter your TikTok password: ')
    blocker = Blocker(email=email, password=password, wait=args.wait, headless=args.headless)

    blocker.login()
    blocker.cycle_block_list()
    blocker.quit()
