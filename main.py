import sys
sys.path.append("..")
from PyInquirer import prompt, Separator

from tikblock.tikblock import ttb
from instablock.instablock import igb
from bloX.blox import xb
from faceblock.faceblock import fbb

logo = """
 ______   _        _______  _______  _       
(  ___ \ ( \      (  ___  )(  ____ \| \    /\\
| (   ) )| (      | (   ) || (    \/|  \  / /
| (__/ / | |      | |   | || |      |  (_/ / 
|  __ (  | |      | |   | || |      |   _ (  
| (  \ \ | |      | |   | || |      |  ( \ \ 
| )___) )| (____/\| (___) || (____/\|  /  \ \\
|/ \___/ (_______/(_______)(_______/|_/    \\/
"""

def main():
    
    questions = [
        {
            'type': 'list',
            'name': 'option',
            'message': 'Choose which Social Media you would like to run the block script on: ',
            'choices': [
                'Instagram',
                'Facebook',
                'X',
                'TikTok',
                Separator(),
                'Exit'
            ]
        }
    ]
    
    while True:
        try:
            print(logo)
            answers = prompt(questions)
            if answers is None:
                print("No option selected. Please try again.")
                continue
            
            choice = answers.get('option')
            if not choice:
                print("Invalid selection. Please try again.")
                continue

            if choice == 'Instagram':
                print("You selected Instagram")
                igb()
            elif choice == 'Facebook':
                print("You selected Facebook")
                fbb()
            elif choice == 'X':
                print("You selected X")
                xb()
            elif choice == 'TikTok':
                print("You selected TikTok")
                ttb()
            elif choice == 'Exit':
                print("Exiting the program.")
                break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
