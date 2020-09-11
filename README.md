# PyAutoGUI
##This Program has been created on Jupyter Notebook using Python3
##Author: Saurav
##Published: 20.04.2020
##Objective: To launch any Desktop application and perform desired operations successfully
##Dependencies: Must have python installed along with pyautogui
##Imp. Functions Used:

      -pyautogui.position(): Takes no argument, returns current cursor position
      -puautogui.click(int x,int y,button_type,clicks,...): Takes multiple arguments such as where to click (x,y), left/right, single/double clicks
      -pyautogui.typewrite("string"): Takes exactly one arguement, whatever goes in as arguement gets typed
      -pyautogui.keyDown('str'): can be any key from the key-board
      -pyautogui.press('str'): takes only 1 arguement of string type having 'tab' as one of its possible values
      -pyautogui.keyUp('str'): opposite to pyautogui.keyDown('str'), ex - when shift is used once, behaves as CAPS ON, second time, turns it off

'''
Solution Approach from scratch for building similar code any other application:

       1.  First of all you must know the x,y position of the window where you want to click. For this, manually lanch the
           desktop application that you want to imitate, place your curser on the desired position over the app, where you
           want to click and then return back to code editor and run pyautogui.position() function, to get the position
           where you want to click.
                     
       2. Then launch application - refer line no. 28 to 32, don't forget to put some sleep in between
                     
       3. After launching application, return back to code editor using tabbing to code further so as to check for
       positions of further clicks in similar fashion
'''

'''Rough-Work:

#Some trial and error

#print(pyautogui.position())
#pyautogui.hotkey('Alt','Tab')
#pyautogui.typewrite(['enter'])
#pyautogui.keyDown("shift")
#pyautogui.keyUp("shift")
#pyautogui.keyDown('7')
#pyautogui.click(1630,452)
#print(pyautogui.position())
