# extras.py
# Includes various functions and code that all seperate simulations may need to make use of preventing code repitition
# Ethan Peterson
# April 19, 2017

# scene parameter takes scene object to properly close the window and detect key presses when that window is selected
def keyPress(scene): # handles key press events in all simulations
    if scene.kb.keys: # wait for key event to be processed
        key = scene.kb.getkey() # get last key to be to be pressed
        if key == 'esc': # if the user pressed the escape key exit the program
            exit()
        elif key == ' ':
            while True:
                ev = scene.waitfor('keydown')
                if ev.key == 'p':
                    break