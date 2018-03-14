# Ethan Peterson
# Circular Motion Simulation
# Reference https://github.com/gcschmit/vpython-physics/blob/master/circular%20motion/circularMotion.py


# Import Relevant Libraries
from visual import * # VPython Libs
import numpy # NumPy lib for access to additional mathematical operations with python 
# used in this case for sine and cosine functions
from visual.graph import * # graphing libs
from extras import * # misc extras that may be useful

# Constants

gravity = vector(0, 9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations. (m/s/s)
# See Documentation: http://vpython.org/contents/docs/vector.html

length = 10 # length of the string in m
theta = 0 # in Rad

diameter = 2 # the diameter of the ball
string = cylinder(pos=(0, 0, 0), axis=(0, -length, 0), radius=0.1)
ball = sphere(pos=(0, -length - 0.5 * diameter, 0), radius=0.5 * diameter, color=color.red)
period = 1.0 # in seconds
ballMass = 0.1 # in Kg
ballW = vector(0, 0, 2 * pi / period) # since omega is equal to 2pi * 1/T
ballVel = cross(ballW, string.axis) # velocity is the cross product of these two vectors
radius = length # radius of the circle formed by the motion of the ball

# Time Related Constants

t = 0 # logs the total time the fall takes in seconds
dt = 0.01 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs

while True:
    rate(100)
    # centripetal force is the net force
    # the force is the triple scalar product of velocity omega and mass
    Fnet = ballMass * cross(ballW, ballVel)

    # use Newton's Second law to determine acceleration
    a = Fnet / ballMass

    # Calculate resulting velocity
    ballVel += a * dt

    # update string axis allowing it to remain connected to the ball
    string.axis = rotate(string.axis, angle=(mag(ballW) * dt))
    ball.pos = string.axis

    t += dt