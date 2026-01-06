#------ import ------
import datetime
import keyboard
import time
#------ functions ------
def imput_time():
    """
    Function that allows you to choose a departure time on the clock
    """
    global h,m,s
    while True:
        try : 
            h = int(input("Enter an hour 0/24 : "))
            m = int(input("Enter a minute  : "))
            s = int(input("Enter a second  : "))
            if (0 <= h < 24) and (0 <= m < 60) and (0 <= s < 60):
                break
            print("Please enter a valid time")
        except:
            print("Please enter only number")
def print_time():
    """
    Function that print time from the system clock
    """
    while True:
        hours = datetime.datetime.now()
        print(f"Press 'A' to stop. {hours.strftime("%H:%M:%S")}", end="\r")
        time.sleep(1)
        if keyboard.is_pressed('a'):
            choice()

def set_time(h,m,s):
    """
    Docstring for set_time
    
    Function that print time from a set time
    """
    while True:
        print(f"Press 'A' to stop. /n {h:02}:{m:02}:{s:02}", end="\r")
        if keyboard.is_pressed('a'):
            choice()
        temp = h * 3600 + m * 60 + s
        temp += 1
        h = (temp // 3600) % 24
        m = (temp % 3600) // 60
        s = temp % 60
        time.sleep(1)

def choice():
    imput = input("Do you want to set the time? (y/n): ")
    if imput == "y":
        imput_time()
        set_time(h,m,s)
    else:
        print_time()