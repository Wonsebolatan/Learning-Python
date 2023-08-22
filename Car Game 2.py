"""
Modifying instructor code to include the following
if car has already started, print - car has already started, if start is entered again.
if car has stopped, print - car has already stopped, if stopped is entered again.
"""
command = ""

while True:
    status = command
    command = input("> ").lower()

    if command == "start":
        if status == "start":
            print("car has already started")
        else:
            print('Car started... Ready to go!')
    elif command == "stop":
        if status == "stop":
            print("car has already stopped")
        else:
            print('Car stopped.')
    elif command == "help":
        print("""start - to start the car
stop - to stop the car'
quit - to exit """)
    elif command == 'exit':
        break
    else:
        print(" Sorry. I don't understand that!")

"""
Instructor Solution

command = ""
started = False
while True:
    status = command
    command = input("> ").lower()

    if command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print('Car started... Ready to go!')
    elif command == "stop":
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print('Car stopped.')
    elif command == "help":
        print('''start - to start the car
stop - to stop the car'
quit - to exit ''')
    elif command == 'exit':
        break
    else:
        print(" Sorry. I don't understand that!")
"""