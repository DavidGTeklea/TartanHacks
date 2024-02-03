import pynput, time, pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

def pause(x):
    time.sleep(x)

# have your character to do a jump
def jump():
    keyboard.press(Key.space)
    
    # pause for 5 seconds
    pause(5) 
    ''' keyboard.release doesn't work for stopping actions well without setting 
            some kind of sleep delay Toby. Keshav is fine with sleep delay since it only 
            affects one thread instead of the whole program '''
    
    keyboard.release(Key.space)

# have your character do walk a bit
def walk():
    keyboard.press('w')
    
    # pause for 5 seconds
    pause(5) # look at stuff for jump if confused
    
    keyboard.release('w')

def select_sword():
    pyautogui.press('2')

def select_axe():
    pyautogui.press('3')



# these commands differentiate between jumping and walking. use for testing.
# pause(2)
# jump()
# walk()    

 


