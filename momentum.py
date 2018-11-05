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
from visual.graph import * # graphing libs
from extras import * # misc extras that may be useful

# Constants

gravity = vector(0, 9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations. (m/s/s)
# See Documentation: http://vpython.org/contents/docs/vector.html

length = 10 # length of the pendulum string in m
initAngle = 1.5 # The Initial angle of one of the pendulums in radians
theta = 0

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

# Set Up Graphs
graph = gdisplay(x=500, y=0, width=600, height=600, # setup graph display
            title='Theta (rad), X-Pos and Y-Pos',
            xtitle='Time (seconds)', ytitle='Magnitude',
            foreground=color.black, background=color.white)

graphAngle = gcurve(gdisplay = graph, color = color.blue) # Theta value will appear in blue
graphX = gcurve(gdisplay = graph, color = color.black) # X-Pos will appear in black
graphY = gcurve(gdisplay = graph, color = color.red) # Y-Pos will appear in red

def updatePos(rightInMotion, time): # takes boolean indicating which pendulum starts in motion and the time elapsed to update the position
    theta = initAngle * numpy.cos((gravity.y/length) ** (0.5) * time) # Theta as a function of time taken from http://www.leonhostetler.com/blog/newtons-cradle-in-visual-python-201702/
    # double ** symbol is raising to a power
    position = vector(length * numpy.sin(theta), -length * numpy.cos(theta), 0)
    if rightInMotion:
        balls[0].pos = position
        strings[0].axis = position
    else:
        # 
        balls[1].pos = [position.x - diameter, position.y, position.z] # offset for diameter in x dir
        strings[1].axis = position
    # Update Graphs
    graphAngle.plot(pos = (t, theta))
    graphX.plot(pos = (t, position.x)) # use pos variable so we are always graphing the ball in motion
    graphY.plot(pos = (t, position.y))
    # switch pendulums when theta is 0 (add <= in if statement just in case it passes 0 between refreshes)
    if theta <= 0:
        return False
    else:
        return True

rightInMotion = True # start with the right pendulum in motion
while True:
    rate(1.0 / dt)
    rightInMotion = updatePos(rightInMotion, t)
    t += dt