from tikblock.tt_block_list import to_be_blocked
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
from argparse import ArgumentParser
from time import sleep
import sys
# for cross compatibility with python 2/3
if sys.version[0] == '3': raw_input=input 

class Blocker():
    def __init__(self, email, password, wait=8):
        self.driver = webdriver.Firefox()
        self.email = email
        self.password = password
        self.wait = wait
    
    def quit_driver(self):
        self.driver.quit()
        
    def login(self):
        self.driver.get('https://www.tiktok.com/login/phone-or-email/email')
        print('Logging in...')
        sleep(self.wait)
        email_el = self.driver.find_element(By.NAME, 'username')
        password_el = self.driver.find_element(By.CSS_SELECTOR, '.tiktok-wv3bkt-InputContainer.etcs7ny1')
        email_el.send_keys(self.email)
        password_el.send_keys(self.password)
        print('Be ready to complete the CAPTCHA!!!!!')
        password_el.submit()
        sleep(12)
        self.driver.get('https://www.tiktok.com/')
        sleep(self.wait)
        account = self.driver.find_element(By. CSS_SELECTOR, ".css-i6e8iz-ImgAvatar.e14l9ebt18")

        if account:
            print('Logged In :)')

    def cycle_block_list(self):
        print('Beginning block cycle')
        for i in to_be_blocked:
            self.driver.get(i['url'])
            sleep(self.wait)
            dots = self.driver.find_element(By.CSS_SELECTOR, '.css-usq6rj-DivMoreActions.ee7zj8d10')
            actions = ActionChains(self.driver)
            actions.move_to_element(dots).perform()
            sleep(3)
            block_btn = self.driver.find_element(By.CSS_SELECTOR, '.css-51xc1n-DivActionItem.e1vhy9gd2')
            sleep(3)
            block_btn.click()
            sleep(5)
            confirm_btn = self.driver.find_element(By.CSS_SELECTOR, '.e9flc1l5.css-3yqenn-Button-StyledButtonBlock.ehk74z00')
            confirm_btn.click()
            print(f"{i['name']} is now blocked :)")
            sleep(5)
        print('Block cycle complete :)')
            
def ttb():
    while True:
        try:
            email = input("Please enter your TikTok email or username: ")
            password = getpass.getpass('Please enter your TikTok password: ')
            blocker = Blocker(email=email, password=password)

            blocker.login()
            blocker.cycle_block_list()
            blocker.quit_driver()
            break
        except Exception as e:
            print("An error occurred. Waiting for 4 seconds and trying again.")
            blocker.quit_driver()
            sleep(4)