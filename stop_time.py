import time
import keyboard


def stop_time(): # Stop the time
    paused= False
    gap = 0 # counter to remove paused time to actual time

    while True :
        if paused : # If paused
            gap += 1 # Couting every seconds gap if time paused

        real_time= time.time() - gap # remove paused time to actual time
        converted_time = time.strftime("%H:%M:%S", time.localtime(real_time))

        if not paused: # If not paused 
            print("Press '1' to stop time."+ str(converted_time))
        time.sleep(1)

        if keyboard.is_pressed('1'): # Swap into paused or not paused
            if not paused:
                print("Time stopped ! Press '1' to resume."+ str(converted_time)) # Print the time paused 1 time 
                paused = True
            else :
                paused = False
            while keyboard.is_pressed('1'):  # Add debounce for not spamming change
                time.sleep(0.1)
        if keyboard.is_pressed('esc'): # Exit the function
            return

