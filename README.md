# ExitShortcut
Just a simple script to allow you to trigger python scripts like makros by typing text on the keyboard.

## Intallation:
1. install Python3 (from the official python page)
2. Install pip (Download & Run get-pip.py that you will find when searching <a href='https://www.google.com/search?q=python+install+pip&rlz=1C1ONGR_deDE959DE959&oq=python+install+pip&aqs=chrome..69i57j35i39j0i20i263j0l2j0i20i263j0l4.329j0j7&sourceid=chrome&ie=UTF-8'>"python install pip"</a> on Google)
3. install the required python libraries using "pip install -r requirements.txt"

## Usage:
1. Simply ExitShortcut.py 
2. Just type whatever command you want to use in any window (not the command Prompt as it will exit on enter)
3. Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd> to execute the last typed Command

## Default commands:
- hide: Hide the active window
- show: Reopen the last hidden windows (Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Enter</kbd> multiple times to reopen all)
- showall: Reopen all hidden windows
- exit: Close the active window

## Create your own commands:
- create a python file in the commands folder
- define a fuction starting with **cmd_** that will be executed when the string after the underscore is entered (the maximal command lenght is defined in ExitShortcut.py)

