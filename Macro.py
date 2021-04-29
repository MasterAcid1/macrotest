import keyboard  # using module keyboard
import pyautogui
import time
while True:  # making a loop
     # used try so that if user pressed other than the given key error will not be shown
    if keyboard.is_pressed('w'):  # if key 'q' is pressed 
        pyautogui.write('w')
        time.sleep(0.01)
