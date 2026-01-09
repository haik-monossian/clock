from time import print_time, set_time, imput_time
from alarm import alarm
from stop_time import stop_time
from change_format import change_format
import logging

# --- Log Error ---
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s")

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
        except KeyboardInterrupt:
            print("\n\nFunction disable... Please select number 6 for quit !")
            
        except ValueError as e:
            logging.error(f"Main - ValueError: {e}")
            print("Please enter a valid number")