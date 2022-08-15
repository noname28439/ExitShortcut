import os
from pynput import keyboard
import importlib
from inspect import getmembers, isfunction

#Settings:
MAX_KEY_SAVES = 20  #Amount of last typed keys saved in the list (Keywords can never be longer than this number)


commandfiles = [f for f in os.listdir("./commands/") if f.endswith('.py')]
commands = []
for command in commandfiles:
    module = importlib.import_module("commands."+command.replace(".py", ""))
    commands += [(name[4:], fun) for name, fun in getmembers(module, isfunction) if name.startswith("cmd_")]

lastKeys = []
currently_down = []

def check():
    last = "".join(lastKeys)
    print("Entered: "+str(last))

    for name, fun in commands:
        if last.endswith(name):
            fun()


def on_press(key):
    currently_down.append(key)

    if key == keyboard.Key.enter and keyboard.Key.shift in currently_down and keyboard.Key.ctrl_l in currently_down:
        check()
    if len(str(key).replace("'", "")) != 1: return
    key = str(key).replace("'", "")
    global lastKeys
    lastKeys.append(str(key))
    #print(f"{key} --> {lastKeys}")    #shows key inserts
    if len(lastKeys)>MAX_KEY_SAVES:
        lastKeys.pop(0)
    
def on_release(key):
    while key in currently_down: currently_down.remove(key)


keyListener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyListener.start()

input("Press Enter to quit\n")
quit()


