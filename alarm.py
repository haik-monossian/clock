import datetime
import threading
from playsound import playsound
import time
import logging



def alarm():
    """Alarm Function"""
    print("~~~ ALARM CONFIGURATION ~~~")
    print("\x1B[3mCtrl+c for quit\x1B[0m")
    #Loop Alarm Choice
    while True:
        try : 
            alarm_hour = int(input("Enter an hour 0/23 : "))
            alarm_min = int(input("Enter a minute  0/59 : "))
            alarm_second = int(input("Enter a second  0/59 : "))
            if 0 <= alarm_hour <= 23 and 0 <= alarm_min <= 59 and 0<= alarm_second <= 59:
                break
            else:
                print("Hour must be 0-23, minute and secondmust be 0-59")
        except KeyboardInterrupt:
            print("\n\nExiting alarm setup...")
            return
        except ValueError as e:
            logging.error(f"Alarm - ValueError: {e}")
            print("\nPlease enter only number")
            

    #Tuple Alarm Time
    alarm_time = (alarm_hour, alarm_min, alarm_second)

    #Threading Alarm
    alarm_threading = threading.Thread(target=show_alarm, args=((alarm_time),), daemon=True)
    alarm_threading.start()
    print("Alarm activated...")

def show_alarm(alarm_tuple):
    """Play Alarm & Sound"""
    alarm_hour, alarm_min, alarm_second = alarm_tuple
    while True:
        now = datetime.datetime.now()
        if (now.hour == alarm_hour and now.minute == alarm_min and now.second == alarm_second):
            print("\n \n")
            print("IT'S TIME !")
            print(f"ALARM - Is : {alarm_hour} : {alarm_min} : {alarm_second}")
            print("======================")
            threading.Thread(target=playsound, args=("alarm.mp3",), daemon=True).start()
            break
        time.sleep(1) #Check 1 second
