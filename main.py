from modules.time import print_time, set_time, imput_time
from modules.alarm import alarm
from modules.stop_time import stop_time
from modules.change_format import change_format

def menu():
    while True:
        try:
            print("\n===== MENU =====")
            print("1.  Show Clock ")
            print("2.  Set time ") 
            print("3.  Alarm  ") 
            print("4.  Stop time ") 
            print("5.  AM / PM ") 
            print("6.  Quit ")
            
            choice = int(input("Select a choice : "))
            
            # Structure match / case
            match choice:
                case 1:
                    print_time()
                case 2:
                    my_tuple = imput_time()
                    set_time(my_tuple)
                case 3:
                    alarm()
                case 4:
                    stop_time()
                case 5:
                    change_format()
                case 6:
                    print("Goodbye!")
                    exit()
                case _:  # Default case for unmatched values
                    print("Please enter a number between 1 and 6")

        except ValueError:
            print("Please enter a valid number")
            continue

menu()