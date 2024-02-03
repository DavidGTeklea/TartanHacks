import pynput, time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def pause(x):
    time.sleep(x)

def jump():
    keyboard.press(Key.space)
    
    # pause for 5 seconds
    pause(5) # keyboard.release doesn't work for stopping actions well without setting 
            # some kind of sleep delay Toby. Keshav is fine with sleep delay since it only 
            # affects one thread instead of the whole program
    
    keyboard.release(Key.space)

def walk():
    keyboard.press('w')
    
    # pause for 5 seconds
    pause(5) # look at stuff for jump if confused
    
    keyboard.release('w')


pause(5)

jump()
walk()    

