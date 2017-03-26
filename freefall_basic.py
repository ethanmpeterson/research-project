# Ethan Peterson
# Basic freefall simulation where friction / air resistance is ignored

from visual import *
from visual.graph import *


# Modify these variables to change properties of the simulation
            # -9.8 m/s/s
gravity = vector(0, -9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations.
# See Documentation: http://vpython.org/contents/docs/vector.html

groundStartPos = vector(0, -10, 0) # starting position of the ground onscreen (in metres)
ballStartPos = vector(0, 300, 0) # starting position of the ball which will be in freefall (in metres)
ballVel = vector(0, 0, 0) # starting velocity of the ball in m/s

# Time Related Constant Variables

t = 0 # logs the total time the fall takes in seconds
dt = 0.01 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs

# Set up visuals

ballScene = display (x=0, y=0, width = 500, height = 500, autoscale = true, background=color.blue) # creates the window where our simulation will be shown
ground = box(pos = groundStartPos, size = (800,20,200), material = materials.earth) # creates the ground with the earth texture, which the ball will fall towards
ball = sphere(pos = ballStartPos, radius = 10, material = materials.marble) # creates the ball, which will fall towards the ground

#Setup the acceleration and velocity arrows
vArrow = arrow(pos=ball.pos, axis=ballVel, color=color.green)
aArrow = arrow(pos=ball.pos, axis=gravity, color=color.red)

#Setup the graph
graphY = gdisplay(x=500, y=0, width=600, height=600,
            title='Vertical Position(m), Velocity(m/s), and Acceleration(m/s^2)',
            xtitle='Time (seconds)', ytitle='Magnitude',
            foreground=color.black, background=color.white)

graphPos = gcurve(gdisplay = graphY, color = color.yellow)
graphVel = gcurve(gdisplay = graphY, color = color.green)
graphAcc = gcurve(gdisplay = graphY, color = color.red)

# simulation loop

while ball.pos.y >= 0:
    rate(100)

    # calulcate ball velocity
    ballVel = ballVel + gravity * dt # Same as formula: v2 = v1 + a * dt
    ball.pos += ballVel * dt # update balls position using the velocity value calculated above




