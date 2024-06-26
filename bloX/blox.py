from bloX.x_block_list import to_be_blocked
from selenium import webdriver
from selenium.webdriver.common.by import By 
import getpass
from argparse import ArgumentParser 
from time import sleep
import sys
# for cross compatibility with python 2/3
if sys.version[0] == '3': raw_input=input

class Blocker():
    def __init__(self, username, password, wait=8):
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
        self.wait = wait
        
    def quit_driver(self):
        self.driver.quit()
        
    def login(self):
        self.driver.get('https://x.com/i/flow/login')
        sleep(self.wait)
        print('Logging in...')
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
        sleep(self.wait)
        password_btn = self.driver.find_element(By.CSS_SELECTOR, '.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')
        password_btn.click()
        sleep(self.wait)
        account = self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r.r-1awozwy.r-sdzlij.r-6koalj.r-18u37iz.r-xyw6el.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        
        if account:        
            print('Logged in :)')
        
    def cycle_block_list(self):
        print('Beginning block cycle')
        for i in to_be_blocked:
            self.driver.get(i['url'])
            sleep(self.wait)
            dots = self.driver.find_element(By.CSS_SELECTOR, '.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-6gpygo.r-1wron08.r-2yi16.r-1qi8awa.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')
            dots.click()
            sleep(5)
            block = None
            btns = self.driver.find_elements(By.CSS_SELECTOR, '.css-175oi2r.r-1loqt21.r-18u37iz.r-1mmae3n.r-3pj75a.r-13qz1uu.r-o7ynqc.r-6416eg.r-1ny4l3l')
            for b in btns:
                kids = b.find_elements(By.XPATH, './*')
                for k in kids:
                    if "Block" in k.text:
                        block = b 
            block.click()
            sleep(5)
            confirm = None
            confirm_btns = self.driver.find_elements(By.CSS_SELECTOR, '.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-16y2uox.r-6gpygo.r-1udh08x.r-1udbk01.r-3s2u2q.r-peo1c.r-1ps3wis.r-cxgwc0.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l')
            for c in confirm_btns:
                child = c.find_elements(By.XPATH, './*')
                for ch in child:
                    if ch.text == 'Block':
                        confirm = c
            confirm.click()
            print(f"{i['name']} is now blocked :)")
            sleep(self.wait)
        print('Block cycle complete :)')
             
def xb():
    while True:
        try:
            username = input("Please enter yor X username: ")
            password = getpass.getpass("Please enter your X password: ")
            blocker = Blocker(username=username, password=password)
            
            blocker.login()
            blocker.cycle_block_list()
            blocker.quit_driver()
            break
        except Exception as e:
            print("An error occurred. Waiting for 4 seconds and trying again.")
            blocker.quit_driver()
            sleep(4)