import sys
import numpy as np
import matplotlib.pyplot as plt


import pyautogui



    
def show(recog):
    
   
    x,y = pyautogui.position()

    if recog == 'left':
       print("moving mouse .......!")
       x = x - 25

    if recog == 'right':
        print("moving mouse .......!")
        x = x + 25

    if recog == 'up':
        print("moving mouse .......!")
        y = y - 25

    if recog == 'down' or recog== 'don':
        print("moving mouse .......!")
        y = y + 25

    pyautogui.moveTo(x, y)

    if recog == 'click':
        print("click mouse .......!")
        pyautogui.click()

    if recog == 'right click':
        print("right clicking mouse .......!")
        pyautogui.click(button='right')

    if recog == 'double click':
        print("double clicking mouse .......!")
        pyautogui.click(clicks=2, interval=0.25)

                        
    if recog == 'scroll up':
        print("scrolling up mouse .......!")
        pyautogui.scroll(10)

    if recog == 'scroll down':
        print("scrolling down mouse .......!")
        pyautogui.scroll(-10)

    if recog == 'close':
        print("closing mouse .......!")
        exit()