import datetime
import threading
from playsound import playsound
import time

def alarm():
    """Alarm Function"""
    print("~~~ ALARM CONFIGURATION ~~~")
    #Loop Alarm Choice
    while True:
        try : 
            alarm_hour = int(input("Enter an hour 0/23 : "))
            alarm_min = int(input("Enter a minute  0/60 : "))
            if 0 <= alarm_hour <= 23 and 0 <= alarm_min <= 59:
                break
            else:
                print("Hour must be 0-23 and minute must be 0-59")
        except:
            print("Please enter only number")

    #Threading Alarm
    alarm_threading = threading.Thread(target=show_alarm, args=(alarm_hour, alarm_min), daemon=True)
    alarm_threading.start()
    print("Alarm activated...")

def show_alarm(alarm_hour, alarm_min):
    """Play Alarm & Sound"""
    while True:
        now = datetime.datetime.now()
        if now.hour == alarm_hour and now.minute == alarm_min:
            print("")
            print("IT'S TIME !")
            print(f"ALARM - Is : {alarm_hour} : {alarm_min}")
            print("======================")
            threading.Thread(target=playsound, args=("alarm.mp3",), daemon=True).start()
            break
        time.sleep(1) #Check 1 second
