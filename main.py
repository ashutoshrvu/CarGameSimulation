command = ""
started = False
while True:
    command = input ("- ").lower()
    if command == "start":
        if started:
            print("The car has already started.")
        else:
            started = True
            print("Car is ready to go!")
    elif command == "stop":
        if not started:
            print("The car is already stationary.")
        else:
            started = False
            print("Car has stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game""")
    elif command == "quit":
        print("You have successfully exited.")
    else:
        print("Invalid command!")