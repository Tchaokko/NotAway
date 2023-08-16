import time
import keyboard
import subprocess

def typing_value_in_time(value, waiting_time):
    while True:

        print("Pressing the key: 20s")

        keyboard.press(value)
        time.sleep(waiting_time)

def open_notepad_and_create_new_tab(path):
    subprocess.call([path])
    keyboard.press_and_release("ctrl+n")

open_notepad_and_create_new_tab(r"C:\Program Files\Notepad++\notepad++.exe")
typing_value_in_time("a", 20)
