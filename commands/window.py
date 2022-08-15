import win32gui, win32con

hidden_frames = []

def kill_active_frame(win):
    win32gui.PostMessage(win,win32con.WM_CLOSE,0,0)

def hide_active_frame(win):
    hidden_frames.append(win)
    win32gui.ShowWindow(win, 0)
    
def reveal_all_hidden_frames():
    for frame in hidden_frames:
        win32gui.ShowWindow(frame, win32con.SW_SHOWNORMAL)
    while len(hidden_frames)>0:
        hidden_frames.pop(0)

def reveal_last_hidden_frame():
    if len(hidden_frames)>0:
        frame = hidden_frames[-1]
        win32gui.ShowWindow(frame, win32con.SW_SHOWNORMAL)
        hidden_frames.remove(frame)


def cmd_exit():
    kill_active_frame(win32gui.GetForegroundWindow())

def cmd_hide():
    hide_active_frame(win32gui.GetForegroundWindow())

def cmd_showall():
    reveal_all_hidden_frames()

def cmd_show():
    reveal_last_hidden_frame()

