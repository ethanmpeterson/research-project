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

# Time Related Constants

t = 0 # logs the total time the fall takes in seconds
dt = 0.01 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs
period = 1.0 # in seconds

while True:
    rate(200)
    pass