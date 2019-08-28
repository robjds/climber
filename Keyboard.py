import curses

class robotController:
  def __init__(self, name):
    self.name = name

  def forward(self):
    print(self.name + " forward.")

  def backward(self):
    print(self.name + " backward.")

  def left(self):
    print(self.name + " right.")

  def right(self):
    print(self.name + " right.")

  def stop(self):
    print(self.name + " stop.")

robot = robotController("Climber")

actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
    }

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY DOWN
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            robot.stop()

curses.wrapper(main)
