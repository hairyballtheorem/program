import os
import threading
import pyperclip
from pynput.keyboard import Key, Listener, Controller

controller = Controller()

def t():
    os.system("xclip")

threading.Thread(target=t).start()

def on_press(key):
    if key == Key.space:
        pyperclip.copy("🇺🇸")
        controller.press(Key.backspace)
        controller.release(Key.backspace)
        controller.press(Key.ctrl)
        controller.press("v")
        controller.release("v")
        controller.release(Key.ctrl)

with Listener(on_press=on_press) as l:
    l.join()