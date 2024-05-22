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
        self.driver.get('https://x.com/i/flow/login')
        sleep(self.wait)
        username_el = self.driver.find_element(By.CSS_SELECTOR, '.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7')
        username_el.send_keys(self.username)
        username_btns = self.driver.find_elements(By.CSS_SELECTOR, '.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')
        next_btn = None
        for b in username_btns:
            kids = b.find_elements(By.XPATH, './*')
            for k in kids:
                if k.text == 'Next':
                    next_btn = b
        next_btn.click()
        sleep(self.wait)
        password_el = self.driver.find_element(By.CSS_SELECTOR, '.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7')
        password_el.send_keys(self.password)
        password_btn = self.driver.find_element(By.CSS_SELECTOR, '.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')
        print('Logging in...')
        password_btn.click()
        sleep(self.wait)
        print('Logged in :)')
        
    def cycle_block_list(self):
        print('cycle_block_list called :)')
    
if __name__ == '__main__':
    parser = ArgumentParser(description='Block everyone on the block_list on your X account. Requires Firefox')
    parser.add_argument("--wait", type=float, default=8, help='Explicit wait time between page loads (default to 8 seconds to be safe)')
    parser.add_argument("--headless", action='store_true', help='Run Selenium in headless mode (hide browser window)')
    args = parser.parse_args()
    
    username = input("Please enter yor X username: ")
    password = getpass.getpass("Please enter your X password: ")
    blocker = Blocker(username=username, password=password, wait=args.wait, headdless=args.headless)
    
    blocker.login()
    blocker.cycle_block_list()
    blocker.quit()
        