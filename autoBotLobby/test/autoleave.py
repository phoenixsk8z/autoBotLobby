from pyautogui import *
import time
import keyboard
import random
import win32api, win32con
screenWidth = 1728
screenHeight = 1080
running = True
pyautogui.click(900, 1070)
time.sleep(1)

while running:
    print(pyautogui.position())
"""

    if pyautogui.locateOnScreen('ready.png', region=(), confidence=0.8) != None:
        pyautogui.moveTo(100, 980)
        time.sleep(0.5)
        pyautogui.click()
    
    if pyautogui.locateOnScreen('dropship.png'):
        pyautogui.press('esc')
        print("Pressing ESC & SLEEPING 1 SECOND")
        time.sleep(1)
        print("Moving To Leave Button")
        pyautogui.moveTo(screenWidth / 2, 600)
        print("Sleeping 0.5")
        time.sleep(0.5)
        print("Clicking Leave Button")
        pyautogui.click()
        print("Sleeping 1 Second")
        time.sleep(1)
        print("Moving To Yes Button")
        pyautogui.moveTo(800, 700)
        print("Sleeping 0.5")
        time.sleep(0.5)
        print("Clicking Yes Button")
        pyautogui.click()
"""