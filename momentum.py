# Ethan Peterson
# Newton's Cradle Simulation covering our momentum unit
# NOTE: The ususal universal controls are not applicable for this simulation as the cycling of the newton's cradle is the same at any point in time so they will not be included
# It is assumed both balls are of equal mass for the newton's cradle to work
# http://www.leonhostetler.com/blog/newtons-cradle-in-visual-python-201702/
# ^ is used for reference on how to handle the collision between the two balls

# Import Relevant Libraries
from visual import * # VPython Libs
import numpy # NumPy lib for access to additional mathematical operations with python 
# used in this case for sine and cosine functions

# Constants

gravity = vector(0, 9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations. (m/s/s)
# See Documentation: http://vpython.org/contents/docs/vector.html

length = 10 # length of the pendulum string in m
initAngle = 1.5 # The Initial angle of one of the pendulums in radians
diameter = 2 # the diameter of the balls attached to each pendulum
position = vector(length * numpy.sin(initAngle), -length * numpy.cos(initAngle), 0)
# Create the two pendulums
balls = []
balls.append(sphere(pos=position, radius=0.5 * diameter, color=color.blue)) # the moving sphere / pendulum
            #           x and y pos are the components of the triangle formed
balls.append(sphere(pos=(-diameter, -length, 0), radius=0.5 * diameter, color=color.red)) # pendulum that will start hanging at rest

strings = [] # list of the strings for various pendulums
strings.append(cylinder(pos=(0, 0, 0), axis=(balls[0].pos[0], balls[0].pos[1], 0), radius=0.1))
strings.append(cylinder(pos=(-diameter, 0, 0), axis=(balls[1].pos[0] + diameter, balls[1].pos[1], 0), radius=0.1))

# Time Related Constants

t = 0 # logs the total time the fall takes in seconds
dt = 0.01 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs

def updatePos(rightInMotion, time): # takes boolean indicating which pendulum starts in motion and the time elapsed to update the position
    theta = initAngle * numpy.cos((gravity.y/length) ** (0.5) * time) # Theta as a function of time taken from http://www.leonhostetler.com/blog/newtons-cradle-in-visual-python-201702/
    position = vector(length * numpy.sin(theta), -length * numpy.cos(theta), 0)
    if rightInMotion:
        balls[0].pos = position
        strings[0].axis = position
    else:
        # 
        balls[1].pos = [position.x - 2, position.y, position.z]
        strings[1].axis = position
    # switch pendulums when theta is 0 (add <= in if statement just in case it passes 0 between refreshes)
    if theta <= 0:
        return False
    else:
        return True

rightInMotion = True # start with the right pendulum in motion
while True:
    rate(100)
    rightInMotion = updatePos(rightInMotion, t)
    t += dt