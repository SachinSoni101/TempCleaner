import pyautogui
import os

dir1 = os.listdir("C:/Windows/TEMP")
dir2 = os.listdir("C:/Users/Home/AppData/Local/Temp")

if len(dir1) == 0:
    print("Nothing is there, ")    
    decision = input("type check to check it, else press Enter or you can type exit: ")

    if decision == "Check" or decision == "check" or decision == "CHECK":
        pyautogui.hotkey("win", "r")
        pyautogui.moveTo(758, 745)
        pyautogui.click(button='left')
        pyautogui.moveTo(110, 622)
        pyautogui.click(button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write('TEMP')
        pyautogui.press('enter')

else:
    pyautogui.hotkey("win", "r")
    pyautogui.moveTo(758, 745)
    pyautogui.click(button='left')
    pyautogui.moveTo(110, 622)
    pyautogui.click(button='left')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write("%tmp%")
    pyautogui.press('enter')
    pyautogui.moveTo(490, 280, duration=0.30)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('delete')
    pyautogui.PAUSE = 1
    pyautogui.press('enter')
    print("DONE!")
if len(dir2) == 0:
    print("Nothing is there, ")    
    decision = input("type check to check it, else press Enter or you can type exit")
        
        
    if decision == "Check" or decision == "check" or decision == "CHECK":
        pyautogui.hotkey("win", "r")
        pyautogui.moveTo(758, 745)
        pyautogui.click(button='left')
        pyautogui.moveTo(110, 622)
        pyautogui.click(button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.write("%tmp%")
        pyautogui.press('enter')

else:
    pyautogui.hotkey("win", "r")
    pyautogui.moveTo(758, 745)
    pyautogui.click(button='left')
    pyautogui.moveTo(110, 622)
    pyautogui.click(button='left')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write("TEMP")
    pyautogui.press('enter')
    pyautogui.moveTo(490, 280, duration=0.30)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('delete')
    pyautogui.PAUSE = 1
    pyautogui.press('enter')
    print("DONE!")


