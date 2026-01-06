from alarm import alarm

def menu():
    while True:
        try:
            print("===== MENU =====")
            print("1.  Show Clock "
            "\n2.  Set time " 
            "\n3.  Alarm  " 
            "\n4.  Stop time " 
            "\n5.  AM / PM " 
            "\n6.  Quit ")
            choice = int(input("Select a choice : "))
            1 <= choice <= 6
        except ValueError:
            print("Please enter a number between 1 and 6")
            continue

        if choice == 1:
            pass
        if choice == 2:
            pass
        if choice == 3:
            alarm()
        if choice == 4:
            pass
        if choice == 5:
            pass
        if choice == 6:
            exit()
        

menu()
