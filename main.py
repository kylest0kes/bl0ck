from PyInquirer import prompt, Separator

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
            'message': 'Choose which Social Media ',
            'choices': [
                'Option 1',
                'Option 2',
                'Option 3',
                'Option 4',
                Separator(),
                'Exit'
            ]
        }
    ]

    print(logo)
    
    while True:
        answers = prompt(questions)
        choice = answers['option']

        if choice == 'Option 1':
            print("You selected Option 1")
            # Add functionality for Instagram here
        elif choice == 'Option 2':
            print("You selected Option 2")
            # Add functionality for X here
        elif choice == 'Option 3':
            print("You selected Option 3")
            # Add functionality for Facebook here
        elif choice == 'Option 4':
            print("You selected Option 4")
            # Add functionality for TikTok here
        elif choice == 'Exit':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
