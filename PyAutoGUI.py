##########################################################################################################################    
import pyautogui                        #Importing necessary modules
import time

pyautogui.click(109,1049)               #clicking on the search box
time.sleep(1)
pyautogui.typewrite("cal")              #searching for programs (matching/containing/starting with the word "cal")
time.sleep(1)
pyautogui.typewrite(["enter"])          #hitting the enter-key

time.sleep(1)
pyautogui.keyDown('alt')                #Calculator has opened but currently not in focus, hence tabbing back to Jupyter
pyautogui.press('tab')
time.sleep(0.2)
pyautogui.keyUp('alt')
pyautogui.keyDown('enter')

time.sleep(1)                           #Again tabbing from Jupyter to Calculator (Attention: Note the wait in between)
pyautogui.keyDown('alt')
pyautogui.press('tab')
time.sleep(0.2)
pyautogui.keyUp('alt')
pyautogui.keyDown('enter')

time.sleep(1)
pyautogui.click(1347,612,clicks=2)      #Performing desired operations on Calculator (from line 33 to 41)
time.sleep(1)
pyautogui.click(x=1770, y=776)
time.sleep(1)
pyautogui.click(x=1351, y=785,clicks=2)
time.sleep(1)
pyautogui.keyDown('enter')
time.sleep(1)
pyautogui.click(x=1809, y=128)