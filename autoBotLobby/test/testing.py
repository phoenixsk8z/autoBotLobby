import pyautogui
import pydirectinput
from pyautogui import *
import time
import keyboard
import random
import win32api, win32con
running = True
time.sleep(1)

sleepValues = [0.23, 0.29, 0.54, 0.67, 0.81, 0.43]

liz = [
    [100, 980],
    [000, 000],
    [864, 600],
    [800, 700],
    [000, 000] 
]

while running:
    for item in liz:
        

def readyBtn():
    if running and pyautogui.locateOnScreen('images/readyBtn.png', region=(40, 915, 335, 105), confidence=0.8) != None:
    pydirectinput.moveTo(100, 980)
    sleep(random.choice(sleepValues))
    pydirectinput.click()

def dropshipBtn():
    if running and pyautogui.locateOnScreen('images/dropshipBtn.png', confidence=0.7) != None:
    pydirectinput.press('esc')
    print("Pressing ESC & SLEEPING 1 SECOND")
    time.sleep(1)

def leaveMatchBtn():
    print("Moving To Leave Button")
    pydirectinput.moveTo(864, 600)
    sleep(random.choice(sleepValues))
    print("Clicking Leave Button")
    pydirectinput.click()
    print("Sleeping 1 Second")
    time.sleep(1)
    
def confirmBtn():
    print("Moving To Yes Button")
    pydirectinput.moveTo(800, 700)
    print("Sleeping 0.5")
    sleep(random.choice(sleepValues))
    print("Clicking Yes Button")
    pydirectinput.click()

def spaceContinueBtn():
    pydirectinput.press('space')
    sleep(random.choice(sleepValues))

while running:
    print(random.choice(sleepValues))