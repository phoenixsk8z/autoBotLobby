import pyautogui
import pydirectinput
from pyautogui import *
import time
import keyboard
import random
import win32api, win32con
sleepValues = [0.18, 0.20, 0.21, 0.23, 0.24, 0.25, 0.27, 0.29, 0.30, 0.32, 0.35, 0.36, 0.37, 0.39, 0.43, 0.45, 0.49, 0.54, 0.67]
running = True
time.sleep(1)


while running:

    if running and pyautogui.locateOnScreen('images/readyBtn.png', region=(40, 915, 335, 105), confidence=0.8) != None:
        pydirectinput.moveTo(100, 980)
        sleep(random.choice(sleepValues))
        pydirectinput.click()

    if keyboard.is_pressed('q'):
        running = False

    if running and pyautogui.locateOnScreen('images/dropshipBtn.png', confidence=0.7) != None:
        pydirectinput.press('esc')
        print("Pressing ESC & SLEEPING 1 SECOND")
        time.sleep(1)

    if keyboard.is_pressed('q'):
        running = False
    
    if running and pyautogui.locateOnScreen('images/leaveMatchBtn.png', confidence=0.7) != None:
        print("Moving To Leave Button")
        pydirectinput.moveTo(864, 600)
        sleep(random.choice(sleepValues))
        print("Clicking Leave Button")
        pydirectinput.click()
        print("Sleeping 1 Second")
        time.sleep(1)
    
    if keyboard.is_pressed('q'):
        running = False

    if running and pyautogui.locateOnScreen('images/confirmBtn.png', confidence=0.7) != None:
        print("Moving To Yes Button")
        pydirectinput.moveTo(800, 700)
        print("Sleeping 0.5")
        sleep(random.choice(sleepValues))
        print("Clicking Yes Button")
        pydirectinput.click()
    
    if keyboard.is_pressed('q'):
        running = False

    if running and pyautogui.locateOnScreen('images/spaceContinueBtn.png', confidence=0.7) != None:
        pydirectinput.press('space')
        sleep(random.choice(sleepValues))