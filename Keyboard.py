
import  movementFunctions  as robot

import curses
# curses.noecho()
# curses.cbreak()

def quitter():
    robot.cleanup() # Stop ranging
    print 'bye ...'

import atexit
atexit.register(quitter)

actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
    ord('z'):         robot.openfront,
    ord('x'):         robot.closefront,
    ord('s'):         robot.stop,
    }

def main(window):
    next_key = None
    while True:
        robot.storeData()
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY DOWN
            curses.halfdelay(3)
            # print(key)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            # robot.stop()

curses.wrapper(main)
