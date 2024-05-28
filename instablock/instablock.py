from instablock.ig_block_list import to_be_blocked
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
            option.add_argument("--headless")
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
        self.driver.get('https://www.instagram.com/')
        sleep(self.wait)
        username_el = self.driver.find_element(By.NAME, "username")
        password_el = self.driver.find_element(By.NAME, "password")
        username_el.send_keys(self.username)
        password_el.send_keys(self.password)
        print("Logging in...")
        password_el.submit()

        sleep(self.wait)
        print('Logged in :)')
        
    def cycle_block_list(self):
        print('Beginning block cycle')
        for i in to_be_blocked:
            self.driver.get(i['url'])
            sleep(self.wait)
            elipse = self.driver.find_element(By.CLASS_NAME, "xurb0ha")
            elipse.click()
            sleep(2)
            block_btns = self.driver.find_elements(By.CLASS_NAME, "_a9--")
            block_btn = None
            for b in block_btns:
                if b.text == 'Block':
                    block_btn = b
            block_btn.click()
            sleep(2)
            block_confirm = self.driver.find_element(By.CLASS_NAME, "x1xlr1w8")
            block_confirm.click()
            sleep(2)
            dismiss_btn = self.driver.find_element(By.CLASS_NAME, "x52vrxo")
            dismiss_btn.click()
            print(f"{i['name']} is now blocked :)")
            sleep(2)
        print('Block cycle complete :)')
            

def igb():
    parser = ArgumentParser(description='Block everyone on the block_list on your Instagram. Requires Firefox')
    parser.add_argument("--wait", type=float, default=8, help="Explicit wait time between page loads (default 8 seconds to be safe)")
    parser.add_argument("--headless", action="store_true", help="Run Selenium in headless mode (hide browser window)")
    args = parser.parse_args()
    
    username = input("Please enter your Instagram username: ")
    password = getpass.getpass('Please enter your Instagram password: ')
    blocker = Blocker(username=username, password=password, wait=args.wait, headless=args.headless)

    blocker.login()
    blocker.cycle_block_list()
    blocker.quit()