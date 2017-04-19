# Ethan Peterson
# Basic free fall simulation where friction / air resistance is ignored
# it is assumed the ball is falling in vacuum

from visual import *
from visual.graph import *


# Modify these variables to change properties of the simulation:
                 # x, y, z
gravity = vector(0, -9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations. (m/s/s)
# See Documentation: http://vpython.org/contents/docs/vector.html

groundStartPos = vector(0, -10, 0) # starting position of the ground onscreen (in metres)
ballStartPos = vector(0, 300, 0) # starting position of the ball which will be in freefall (in metres)
ballVel = vector(0, 0, 0) # starting velocity of the ball in m/s
ballMass = 5 # the ball's mass in kg
ballDragCoeff = 1.2 # drag coefficient of the ball
ballNetForce = vector(0, 0, 0) # holds the net force of the ball
ballDrag = vector(0, 0, 0) # holds ball drag force


# Time Related Constants

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
graphY = gdisplay(x=500, y=0, width=600, height=600, # setup graph display
            title='Vertical Position(m), Velocity(m/s), and Acceleration(m/s/s)',
            xtitle='Time (seconds)', ytitle='Magnitude',
            foreground=color.black, background=color.white)

graphPos = gcurve(gdisplay = graphY, color = color.blue) # position will appear in blue on the graph
graphVel = gcurve(gdisplay = graphY, color = color.green) # velocity will appear in green
graphAcc = gcurve(gdisplay = graphY, color = color.red) # acceleration will appear in red

# setup window for live data and additional information
dataWindow = display(x=0, y = 600, width = 1100, height = 150,
                     box = 0, background = color.white, foreground = color.black)

liveMotionData = label(yoffset = 15, xoffset = -110, line = 0)
liveForceData = label(yoffset = 15, xoffset = 110, line = 0)

# simulation loop

while ball.pos.y >= 0:
    rate(100) # set loop to run 100 times a second

    # Calculate ball's drag and net froces
    ballDrag = - ballDragCoeff * ballVel
    ballNetForce = ballMass * gravity + ballDrag


    # calulcate ball velocity
    ballVel += ballNetForce * dt / ballMass
    ball.pos += ballVel * dt

    # Update vector arrows surrounding the ball
    vArrow.pos = ball.pos + (12, 0, 0) # offset position of the arrows so they do not appear inside the ball and on top of each other
    vArrow.axis = 2 * ballVel # multiply velocity by 2 to make vector arrow more visible and larger
    aArrow.pos = ball.pos + (-12, 0, 0) # ^
    aArrow.axis = 2 * ballNetForce / ballMass # multiply by 2 to make acceleration arrow more visible since it remanins constant

    # Update Graphs
    graphPos.plot(pos = (t, ball.pos.y))
    graphVel.plot(pos = (t, ballVel.y))
    graphAcc.plot(pos = (t, ballNetForce.y / ballMass))

    # update data window
    liveMotionData.text = 'Velocity: ' + str(ballVel.y) + ' m/s \n' # gives ball's real time velocity
    liveMotionData.text += 'Position: ' + str(ball.pos.y) + ' m \n' # gives ball's current y pos
    liveMotionData.text += 'Acceleration: ' + str(ballNetForce.y / ballMass) + ' m/s/s'

    liveForceData.text = 'Net Force: ' + str(ballNetForce) + ' N \n'
    liveForceData.text += 'Drag Force: ' + str(ballDrag) + ' N'

    # increment the time
    t += dt