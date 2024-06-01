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
    def __init__(self, username, password, wait=8):
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
        self.wait = wait
    
    def quit_driver(self):
        self.driver.quit()
        
    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(self.wait)
        print("Attempting to log in...")
        username_el = self.driver.find_element(By.NAME, "username")
        password_el = self.driver.find_element(By.NAME, "password")
        username_el.send_keys(self.username)
        password_el.send_keys(self.password)
        password_el.submit()
        sleep(self.wait)
        account = self.driver.find_element(By.CSS_SELECTOR, ".xpdipgo.x972fbf.xcfux6l.x1qhh985.xm0m39n.xk390pu.x5yr21d.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xl1xv1r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf.xh8yej3").get_attribute('alt')
        
        if account:
            print('Logged in :)')
        
    def cycle_block_list(self):
        print('Beginning block cycle')
        for i in to_be_blocked:
            self.driver.get(i['url'])
            sleep(self.wait)
            elipse = self.driver.find_element(By.CSS_SELECTOR, ".x1i10hfl.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xcdnw81")
            elipse.click()
            sleep(self.wait)
            block_btns = self.driver.find_elements(By.CSS_SELECTOR, ".xjbqb8w.x1qhh985.xcfux6l.xm0m39n.x1yvgwvq.x13fuv20.x178xt8z.x1ypdohk.xvs91rp.x1evy7pa.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1wxaq2x.x1iorvi4.x1sxyh0.xjkvuk6.xurb0ha.x2b8uid.x87ps6o.xxymvpz.xh8yej3.x52vrxo.x4gyw5p.xkmlbd1.x1xlr1w8")
            block_btn = None
            for b in block_btns:
                if b.text == 'Block':
                    block_btn = b
            block_btn.click()
            sleep(self.wait)
            block_confirm = self.driver.find_elements(By.CSS_SELECTOR, ".xjbqb8w.x1qhh985.xcfux6l.xm0m39n.x1yvgwvq.x13fuv20.x178xt8z.x1ypdohk.xvs91rp.x1evy7pa.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1wxaq2x.x1iorvi4.x1sxyh0.xjkvuk6.xurb0ha.x2b8uid.x87ps6o.xxymvpz.xh8yej3.x52vrxo.x4gyw5p.xkmlbd1.x1xlr1w8")[3]
            block_confirm.click()
            sleep(self.wait)
            print(f"{i['name']} is now blocked :)")
            sleep(self.wait)
        print('Block cycle complete :)')     

def igb():
    while True:
        try:
            username = input("Please enter your Instagram username: ")
            password = getpass.getpass('Please enter your Instagram password: ')
            blocker = Blocker(username=username, password=password)

            blocker.login()
            blocker.cycle_block_list()
            blocker.quit_driver()
            break
        except Exception as e:
            print("An error occurred. Waiting for 4 seconds and trying again.")
            blocker.quit_driver()
            sleep(4)