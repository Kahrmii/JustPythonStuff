#!/user/bin python3
import pyautogui
import keyboard
    
while keyboard.is_pressed('q') == False:
    pyautogui.displayMousePosition()
