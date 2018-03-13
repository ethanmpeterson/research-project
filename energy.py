# Ethan Peterson
# Simulation of Problem 2 on our physics energy test (block slides down ramp friction brings it to a stop after reaching the bottom of the ramp)
# The Block's Motion is broken up into the following events:
# 1. Starts sliding down the ramp
# 2. 

# Import Relevant Libraries
from visual import * # VPython Libs
import numpy # NumPy lib for access to additional mathematical operations with python 
# used in this case for sine and cosine functions
from visual.graph import * # graphing libs
from extras import * # misc extras that may be useful

# Constants 

gravity = vector(0, 9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations. (m/s/s)
# See Documentation: http://vpython.org/contents/docs/vector.html
inclineAngle = 25 # in degrees
theta = inclineAngle * 0.0174533 # convert to RAD to use sin and cos functions in numpy library
blockMass = 2 # in kg (can be changed but default will be identical spec to the problem on the test)
length = 3 # length of the slope in m
startPos = vector(-length * numpy.cos(theta), length * numpy.sin(theta), 0)
blockWidth = 1.0
blockHeight = 0.5
blockStartPos = vector(startPos.x + (blockWidth / 2), startPos.y + (blockHeight / 2), startPos.z)

# use forces to calculate the acceleration down the ramp (resulting velocity will be used to update position and to calculate kinetic energy throughout the motion)



# Time Related Constants

t = 0 # logs the total time the fall takes in seconds
dt = 0.01 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs

# Setup Graphs

# Setup Visuals
ballScene = display (x=0, y=0, width = 500, height = 500, autoscale = true, background=color.black) # creates the window where our simulation will be shown
block = box(pos = blockStartPos, size = (blockWidth, blockHeight, 0), material = materials.marble) # creates the ground with the earth texture, which the ball will fall towards
cylinder(pos=(0, 0, 0), axis=(5,0,0), radius=0.1, color = color.white) # base
cylinder(pos=(0, 0, 0), axis=startPos, radius=0.1, color = color.white) # slope
#ball = sphere(pos = ballStartPos, radius = 10, material = materials.marble) # creates the ball, which will fall towards the ground
while True:
    rate(200)
    t += dt