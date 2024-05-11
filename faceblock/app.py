from selenium import webdriver 
import sys
# for cross compatibility with python 2/3
if sys.version[0] == '3': raw_input=input 

class Blocker():
    def __init__(self, email, password, wait):
        self.Driver = webdriver.Firefox()
        self.email = email
        self.password = password
        self.profile_name = None 
        self.wait = wait
    
if __name__ == '__main__':
    email = raw_input("Please enter your Facebook email: ")
    print(f"User email: {email}")