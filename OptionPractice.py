count = 1
while(1):
    print("Turn: " + str(count))
    print("You see two paths ahead, which way do you go?")
    print("1. Go Left")
    print("2. Go Right")

    pick = "false"

    while(pick == "false"):
        choice = input()
        
        if choice == "1":
            print("You go left.")
            pick = "true"
        elif choice == "2":
            print("You go right.")
            pick = "true"
        else:
            print("Invalid command, try again")
    count += 1
        
