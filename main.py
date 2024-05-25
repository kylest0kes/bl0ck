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
            'message': 'Choose which Social Media you would like to run the block script on: ',
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
            try:
                answers = prompt(questions)
                if answers is None:
                    print("No option selected. Please try again.")
                    continue
                
                choice = answers.get('option')
                if not choice:
                    print("Invalid selection. Please try again.")
                    continue

                if choice == 'Option 1':
                    print("You selected Option 1")
                    # Add functionality for Option 1 here
                elif choice == 'Option 2':
                    print("You selected Option 2")
                    # Add functionality for Option 2 here
                elif choice == 'Option 3':
                    print("You selected Option 3")
                    # Add functionality for Option 3 here
                elif choice == 'Exit':
                    print("Exiting the program.")
                    break
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
