import time
import keyboard

def change_format(): # Change the format 24 into 12 AM PM
    mode = True # initialise mode 24 / 12
    while True: 
        realtime = time.strftime("%H:%M:%S", time.localtime(time.time())) 
        if mode: # Mode 24 H 
            print(realtime, "To change mode press '1', 'esc' to exit")
            time.sleep(1)

        elif not mode: # Mode 12 AM PM 
            if int(realtime[:2]) < 12: # if the hours are < 12 
                print (realtime, " AM","To change mode press '1', 'esc' to exit")
            else :
                new_realtime = str(int (realtime[:2]) - 12) + realtime[2:]
                print ( new_realtime, "PM", ": To change mode press '1', 'esc' to exit")
            time.sleep(1)

        if keyboard.is_pressed('1'): # Press 1 to switch mode 24 / 12
            if mode :
                mode = False
            else : 
                mode = True
        if keyboard.is_pressed('esc'):
            return