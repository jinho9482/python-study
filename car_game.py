# init = input()
# if init == "help":
#     print("start - to start the car")
#     print("stop - to stop the car")
#     print("quit - to exit")

# while True:
#     order = input()
#     if order == "start":
#         print("Car started...Ready to go!")
#     elif order == "stop":
#         print("Car stopped.")
#     elif order == "quit":
#         break
#     else:
#         print("I don't understand that...")

command = ""
started = False
while True:
    command = input("> ")
    if command == "start":
        if not started:
            started = True
            print("Car started...Ready to go!")
        else:
            print("Car already started")
    elif command == "stop":
        if started:
            started = False
            print("Car stopped")
        else:
            print("Car already stopped")
    elif command == "help":
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    else:
        print("I don't understand that...")
