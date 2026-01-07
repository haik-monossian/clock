import time
import keyboard

def change_format():
    mode = True
    try:
        while True:
            now_tuple = time.localtime()
            hours, mins, secs = now_tuple.tm_hour, now_tuple.tm_min, now_tuple.tm_sec
            realtime = f"{hours:02}:{mins:02}:{secs:02}"

            if mode:
                print(realtime, "Pour changer de mode presse '1', 'esc' pour quitter", end="\r")
                time.sleep(1)
            elif not mode:
                if hours < 12:
                    print(realtime, "AM", "Pour changer de mode presse '1', 'esc' pour quitter", end="\r")
                else:
                    hours_pm = hours - 12 if hours > 12 else 12
                    new_realtime = f"{hours_pm:02}:{mins:02}:{secs:02}"
                    print(new_realtime, "PM", ": Pour changer de mode presse '1', 'esc' pour quitter", end="\r")
                time.sleep(1)

            if keyboard.is_pressed('1'):
                mode = not mode
            if keyboard.is_pressed('esc'):
                return
            
            pass

    except KeyboardInterrupt:
        print("\nArrêt du programme avec Ctrl+C !")