# Ethan Peterson
# Simulation of Problem 2 on our physics energy test (block slides down ramp friction brings it to a stop after reaching the bottom of the ramp)
# The Block's Motion is broken up into the following events:
# 1. Starts sliding down the ramp
# 2. reaches the bottom of the ramp
# 3. Friction brings the block to a stop

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
blockVel = vector(0, 0, 0) # initial velocity of the block (starts at rest)
mu = 0.65 # coefficient of friction

# use forces to calculate the acceleration down the ramp (resulting velocity will be used to update position and to calculate kinetic energy throughout the motion)
a = vector(0,0,0)
Fg = vector((blockMass * gravity.y) * numpy.sin(theta), (blockMass * gravity.y) * numpy.cos(theta), blockMass * gravity.y) # z value will simply be overall magnitude of Fg
# coordinate system is on an angle of 25 degrees so we must use trig to get x and y components of Fg
# multiplying Fg by sin of the angle for x comp and by cos for y comp
Fnet = Fg.x # net force is the x component of gravity
a.x = Fnet / blockMass # calculate acceleration derived from formula Fnet = ma
a.y = a.x * numpy.tan(theta) # use trig to inferr acceleration for y - dir since we defined coordinate system on angle
print(a)

# Define Energy Variables
Ek = 0
Eg = 0
Eth = 0

# Time Related Constants

t = 0 # logs the total time the fall takes in seconds
dt = 0.01 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs

# Setup Graphs

graph = gdisplay(x=500, y=0, width=600, height=600, # setup graph display
            title='Ek, Eg, Eth',
            xtitle='Time (seconds)', ytitle='Magnitude (J)',
            foreground=color.black, background=color.white)

graphEk = gcurve(gdisplay = graph, color = color.blue) # Ek will appear in blue on the graph
graphEg = gcurve(gdisplay = graph, color = color.green) # Eg will appear in green
graphEth = gcurve(gdisplay = graph, color = color.red) # Eth will appear in red

# Setup Visuals
scene = display (x=0, y=0, width = 500, height = 500, autoscale = true, background=color.black) # creates the window where our simulation will be shown
block = box(pos = blockStartPos, size = (blockWidth, blockHeight, 0), material = materials.marble) # creates the ground with the earth texture, which the ball will fall towards
base = cylinder(pos=(0, 0, 0), axis=(5,0,0), radius=0.1, color = color.white) # base
slope = cylinder(pos=(0, 0, 0), axis=startPos, radius=0.1, color = color.white) # slope


while True:
    rate(200)
    keyPress(scene)
    if block.pos.x < blockWidth / 2: # When block is sliding down the ramp
        # dt is such a small number that we are calculating the AROC on such a small interval that we are more or less getting instantaneous values (Calculus Application)
        blockVel = blockVel + (a * dt)
        #blockVel.y = blockVel.y + (a.y * dt)
        block.pos.x += blockVel.x * dt
        block.pos.y -= blockVel.y * dt
        # Calculate Energies
        Ek = 0.5 * blockMass * (sqrt((blockVel.x ** 2) + (blockVel.y ** 2)) ** 2)
        Eg = blockMass * gravity.y * block.pos.y
        graphEk.plot(pos = (t, Ek))
        graphEg.plot(pos = (t, Eg))
        graphEth.plot(pos = (t, Eth))
    else: # handle second interval of time at the base of the slope where friction brings the block to a stop
        # calculate negative acceleration due to friction (friction is net force)
        a.y = 0
        Fnet = mu * (gravity.y * blockMass)
        a.x = -(Fnet / blockMass)
        if blockVel.x >= 0:
            blockVel = blockVel + (a * dt)
            block.pos.x += blockVel.x * dt
            # Calculate Energies
            Ek = 0.5 * blockMass * (blockVel.x ** 2)
            Eg = 0
            Eth = Fnet * block.pos.x
            graphEk.plot(pos = (t, Ek))
            graphEg.plot(pos = (t, Eg))
            graphEth.plot(pos = (t, Eth))
        if blockVel.x <= 0:
            break
    t += dt

while True: # keep program running at slower speed without time incrimentation
    rate(30)
    keyPress(scene)
