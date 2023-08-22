"""
prompt > with option for help, start, stop, and exit, all other input produce - 'I don't understand that...'
help whether lowercase or uppercase should print
'start - to start the car'
'stop - to stop the car'
'quit - to exit'
start  - would print 'Car started...Ready to go!
stop - would print 'Car stopped'
quit - exit the game
"""

initiate_game = 0
while initiate_game < 1:
    choice = input('> ')
    if choice.lower() == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif choice.lower() == 'start':
        print('Car started... Ready to go!')
    elif choice.lower() == 'stop':
        print('Car stopped.')
    elif choice.lower() == 'quit':
        break
    else:
        print("I don't understand that...")

"""
Instructor solution
command = ""
while command True:
    command = input("> ").lower()
    if command == "start":
        print('Car started... Ready to go!')
    elif command = "stop":
        print('Car stopped.')
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car'
quit - to exit
        ''')
    elif command == 'exit'
        break
    else:
        print(" Sorry. I don't understand that!")
command = ""
while command True:
    command = input("> ").lower()
    if command == "start":
        print('Car started... Ready to go!')
    elif command = "stop":
        print('Car stopped.')
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car'
quit - to exit
        ''')
    elif command == 'exit'
        break
    else:
        print(" Sorry. I don't understand that!")
"""




