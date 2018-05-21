# Ethan Peterson
# Pendulum Motion Simulation
# Reference https://github.com/gcschmit/vpython-physics/blob/master/circular%20motion/circularMotion.py


# Import Relevant Libraries
from visual import * # VPython Libs
import numpy # NumPy lib for access to additional mathematical operations with python 
# used in this case for sine and cosine functions
from visual.graph import * # graphing libs
from extras import * # misc extras that may be useful

# Constants

g = 9.81 # gravity constant 

length = 10 # length of the string in m
theta = 0 # in Rad

diameter = 2 # the diameter of the ball
rod = cylinder(pos=(0, 0, 0), axis=(0, -length, 0), radius=0.1)
ball = sphere(pos=(0, -length - 0.5 * diameter, 0), radius=0.5 * diameter, color=color.red)
ballMass = 0.1 # in Kg
# all calculations will be done in an angular coordinate system with omega and alpha and then converted back to linear values when the ball is animated onscreen
omega = 0 #pi / 2 # initial angular velocity of the ball
alpha = 0 # initial angular acceleration of the ball

radius = length # radius of the circle formed by the motion of the ball

# Time Related Constants

t = 0 # logs the total time the fall takes in seconds
dt = 0.001 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs

while True: # Reference Simulation only ran for one period because it quickly degenerates
    rate(1.0 / dt)
    if theta > 2 * pi: # ensure theta always remains within range of 0 - 2pi
        theta -= 2 * pi

    alpha = - g * cos(theta) / radius # calculate 
    omega += alpha * dt
    theta += omega * dt
    
    ball.pos = (radius * cos(theta), radius * sin(theta), 0) # convert to linear coordinates and adjust ball pos
    rod.axis = ball.pos
    #t += dt