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
    def __init__(self, email, password, wait=6, headless=False):
        if headless:
            option = webdriver.FirefoxOptions()
            option.add_argument("--headless")
            self.driver = webdriver.Firefox(options=option)
        else:
            self.driver = webdriver.Firefox()
        self.email = email
        self.password = password
        self.wait = wait
        self.profile_name = None
    
    def quit(self):
        self.driver.quit()
        
    def login(self):
        self.driver.get('https://www.facebook.com/login/')
        sleep(self.wait)
        email_element = self.driver.find_element(By.ID, 'email')
        email_element.send_keys(self.email)
        password_element = self.driver.find_element(By.ID, 'pass')
        password_element.send_keys(self.password)
        password_element.submit()
        
        sleep(self.wait)
        username = self.driver.find_element(By.CSS_SELECTOR, 'x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xe8uvvx.xdj266r.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1n2onr6.x87ps6o.x1lku1pv.x1a2a7pz.x78zum5.x1emribx').get_attribute('aria-label')
        # username_val = username
        
        print(username)
        
    def cycle_block_list(self):
        pass
        
    
if __name__ == '__main__':
    parser = ArgumentParser(description='Block everyone on the block_list on your Facebook. Requires Firefox')
    parser.add_argument("--wait", type=float, default=6, help="Explicit wait time between page loads (default 10 seconds to be safe)")
    parser.add_argument("--headless", action="store_true", help="Run Selenium in headless mode (hide browser window)")
    args = parser.parse_args()
    
    email = input("Please enter your facebook email: ")
    password = getpass.getpass('Please enter your Facebook password: ')
    blocker = Blocker(email=email, password=password, wait=args.wait, headless=args.headless)

    blocker.login()
    # blocker.cycle_block_list()
    # blocker.quit()
