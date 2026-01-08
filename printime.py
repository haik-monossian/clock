#------ import ------
import datetime
import keyboard
import time
import pyttsx3



#------ functions ------

def imput_time():
    """
    Prompts the user to enter a time manually via the console.
    Handles ValueError to ensure only integers are accepted.

    Returns:
        tuple: A tuple containing (hours, minutes, seconds) verified within valid ranges.
    """
    while True:
        try: 
            h = int(input("Enter an hour (0-23): "))
            m = int(input("Enter a minute (0-59): "))
            s = int(input("Enter a second (0-59): "))
            
            # Verification
            if (0 <= h < 24) and (0 <= m < 60) and (0 <= s < 60):
                return (h, m, s) # Return the tuple if valid
            
            print("Error: Please enter a valid time range.")

        except KeyboardInterrupt:
            print("\n \nBack to the menuuuuu.\n")
            break
        except ValueError:
            print("Error: Please enter numbers only.")

def print_time():
    """
    Displays the current system time in real-time.
    Runs in an infinite loop until the user presses 'A'.
    """
    print("System Clock started. Press 'A' to stop.")
    count = 0
    while True:
        hours = datetime.datetime.now()
        # %H:%M:%S formats the time string 
        # end="\r" returns the cursor to the start of the line instead of a new line

        engine = pyttsx3.init()
        engine.say(f"il est  : {hours.strftime('%H:%M:%S')}")
        print(f"Current time: {hours.strftime('%H:%M:%S')}   ", end="\r")
        engine.runAndWait()
        engine.stop()
        
        
        
        time.sleep(1) # Pause for 1 second to match real-time
        
        if keyboard.is_pressed('a'):
            print("\nStop requested.")
            return

def set_time(time_tuple):
    """
    Displays a custom clock starting from a specific time tuple.
    Increments the time by one second at each iteration.

    Args:
        time_tuple (tuple): A tuple (hours, minutes, seconds) to start the clock from.
    """
    print("Timer started. Press 'A' to stop.")
    
    while True:
        # Unpack the tuple into individual variables
        h, m, s = time_tuple
        
        # :02 ensures the number is displayed with at least 2 digits 
        print(f"Elapsed time: {h:02}:{m:02}:{s:02}   ", end="\r")
        
        # Check for exit condition before processing calculation
        if keyboard.is_pressed('a'):
            print("\nStop requested.")
            return
            
        # --- Time Calculation Logic ---
        temp = h * 3600 + m * 60 + s
        
        # Increment by one second
        temp += 1
        
        # Convert total seconds back to Hours/Minutes/Seconds
        h = (temp // 3600) % 24 
        m = (temp % 3600) // 60 
        s = temp % 60          
        
        time.sleep(1)
        
        # Create a new tuple with updated values
        time_tuple = (h, m, s)

def choice():
    """
    Main menu function.
    Asks the user to choose between manual time setting or system time.
    """
    user_input = input("Do you want to manually set the time? (y/n): ")
    
    if user_input.lower() == "y": # .lower() handles both 'Y' and 'y'
        time_tuple = imput_time() 
        set_time(time_tuple)      
    else:
        print_time()

