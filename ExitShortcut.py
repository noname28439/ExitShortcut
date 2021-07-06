from pynput import keyboard
import win32gui
import win32con

hidden_frames = []

def kill_active_frame(win):
    win32gui.PostMessage(win,win32con.WM_CLOSE,0,0)

def hide_active_frame(win):
    hidden_frames.append(win)
    win32gui.ShowWindow(win, 0)
    
def reveal_all_hidden_frames():
    for frame in hidden_frames:
        win32gui.ShowWindow(frame, win32con.SW_SHOWNORMAL)

lastKeys = []

currently_down = []

def check():
    print(lastKeys)
    last = ""
    for c in lastKeys:
        last += c
    print("Last: "+str(last))

    #functions
    if last == "exit":
        kill_active_frame(win32gui.GetForegroundWindow())
    
    if last == "hide":
        hide_active_frame(win32gui.GetForegroundWindow())

    if last == "show":
        reveal_all_hidden_frames()

def on_press(key):
    currently_down.append(key)

    if key == keyboard.Key.enter and keyboard.Key.shift in currently_down and keyboard.Key.ctrl_l in currently_down:
        check()
    if len(str(key).replace("'", "")) != 1: return
    key = str(key).replace("'", "")
    global lastKeys
    lastKeys.append(str(key))
    #print(f"{key} --> {lastKeys}")    #shows key inserts
    if len(lastKeys)>4:
        lastKeys.pop(0)
    
def on_release(key):
    while key in currently_down:
        currently_down.remove(key)

keyListener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyListener.start()

input("Press Enter to quit")
quit()


