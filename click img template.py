#!/user/bin python3
import pyautogui
import keyboard
import win32api, win32con
import time
import pyscreeze

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

def leftclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def rightclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    cord = pyautogui.locateCenterOnScreen('C:\\Users\\%USERS%\\Desktop\\py\\IMGs\\wiederherstellen.png', region=(250,250,800,800), confidence=0.8)
    if cord:
        x,y = cord
        time.sleep(0.1)
        leftclick(x,y)
