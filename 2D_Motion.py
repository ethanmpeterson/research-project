# Ethan Peterson

# VPython Imports
from visual import *
from visual.graph import *
from extras import *
# Modify these variables to change properties of the simulation:
                 # x, y, z
gravity = vector(0, -9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations. (m/s/s)
# See Documentation: http://vpython.org/contents/docs/vector.html

groundStartPos = vector(0, -10, 0) # starting position of the ground onscreen (in metres)
ballStartPos = vector(-450, 300, 0) # starting position of the ball which will be in freefall (in metres)
ballVel = vector(100, 10, 0) # starting velocity of the ball in m/s
ballMass = 5 # the ball's mass in kg
ballDragCoeff = 0.6 # drag coefficient of the ball
ballNetForce = vector(0, 0, 0) # holds the net force of the ball
ballDrag = vector(0, 0, 0) # holds ball drag force
ballMomentum = vector(0, 0, 0) # holds the momentum of the ball during the projectile motion

# Time Related Constants

t = 0 # logs the total time the fall takes in seconds
dt = 0.01 # deltaT variable used for calculations as it will be the difference in time between each time the loop runs

# Set up visuals

ballScene = display (x=0, y=0, width = 500, height = 500, autoscale = true, background=color.blue) # creates the window where our simulation will be shown
ground = box(pos = groundStartPos, size = (800,20,200), material = materials.earth) # creates the ground with the earth texture, which the ball will fall towards
ball = sphere(pos = ballStartPos, radius = 12, material = materials.marble, make_trail = True) # creates the ball, which will fall towards the ground

#Setup the acceleration and velocity arrows
vArrow = arrow(pos=ball.pos, axis=ballVel, color=color.green)
aArrow = arrow(pos=ball.pos, axis=gravity, color=color.red)

#Setup the graph
graphY = gdisplay(x=500, y=0, width=600, height=600, # setup graph display
            title='Vertical Position(m), Velocity(m/s), and Acceleration(m/s/s)',
            xtitle='Time (seconds)', ytitle='Magnitude',
            foreground=color.black, background=color.white)

graphX = gdisplay(x=500, y=0, width=600, height=600, # setup graph display
            title='Horizontal Position(m), Velocity(m/s), and Acceleration(m/s/s)',
            xtitle='Time (seconds)', ytitle='Magnitude',
            foreground=color.black, background=color.white)

graphPosY = gcurve(gdisplay = graphY, color = color.blue) # position will appear in blue on the graph
graphVelY = gcurve(gdisplay = graphY, color = color.green) # velocity will appear in green
graphAccY = gcurve(gdisplay = graphY, color = color.red) # acceleration will appear in red

graphPosX = gcurve(gdisplay = graphX, color = color.blue) # position will appear in blue on the graph
graphVelX = gcurve(gdisplay = graphX, color = color.green) # velocity will appear in green
graphAccX = gcurve(gdisplay = graphX, color = color.red) # acceleration will appear in red

# setup window for live data and additional information
dataWindow = display(x=0, y = 600, width = 1100, height = 150,
                     box = 0, background = color.white, foreground = color.black)

liveMotionData = label(yoffset = 0, xoffset = -110, line = 0)
liveForceData = label(yoffset = 15, xoffset = 110, line = 0)
liveMomentumData = label(yoffset = 15, xoffset = 0, line = 0)

# simulation loop

while ball.pos.y >= ground.pos.y:
    rate(100) # set loop to run 100 times a second
    exitOnKeyPress(ballScene)

    # Calculate ball's drag and net froces
    ballDrag = - ballDragCoeff * ballVel
    #ballNetForce.y = ballMass * gravity.y + ballDrag.y # don't apply drag to x axis
    ballNetForce = ballMass * gravity + ballDrag # apply drag to both x and y axis

    # calulcate ball velocity
    ballVel += ballNetForce * dt / ballMass
    ball.pos += ballVel * dt

    # Momentum Update
    ballMomentum += ballNetForce * dt # n/s (newtons per second)

    # Update vector arrows surrounding the ball
    vArrow.pos = ball.pos + (12, 0, 0) # offset position of the arrows so they do not appear inside the ball and on top of each other
    vArrow.axis = 2 * ballVel # multiply velocity by 2 to make vector arrow more visible and larger
    aArrow.pos = ball.pos + (-12, 0, 0) # ^
    aArrow.axis = 2 * ballNetForce / ballMass # multiply by 2 to make acceleration arrow more visible since it remanins constant

    # Update Y Graphs
    graphPosY.plot(pos = (t, ball.pos.y))
    graphVelY.plot(pos = (t, ballVel.y))
    graphAccY.plot(pos = (t, ballNetForce.y / ballMass))

    # Update X Graphs
    graphPosX.plot(pos = (t, ball.pos.x))
    graphVelX.plot(pos = (t, ballVel.x))
    graphAccX.plot(pos = (t, ballNetForce.x / ballMass))

    # update data window
    liveMotionData.text = 'Y Velocity: ' + str(round(ballVel.y, 3)) + ' m/s \n' # gives ball's real time velocity
    liveMotionData.text += 'Y Position: ' + str(round(ball.pos.y, 3)) + ' m \n' # gives ball's current y pos
    liveMotionData.text += 'Y Acceleration: ' + str(round((ballNetForce.y / ballMass), 3)) + ' m/s/s \n \n'

    liveMotionData.text += 'X Velocity: ' + str(round(ballVel.x, 3)) + ' m/s \n' # gives ball's real time velocity
    liveMotionData.text += 'X Position: ' + str(round(ball.pos.x, 3)) + ' m \n' # gives ball's current y pos
    liveMotionData.text += 'X Acceleration: ' + str(round((ballNetForce.x / ballMass), 3)) + ' m/s/s'

    liveForceData.text = 'Y Net Force: ' + str(round(ballNetForce.y, 3)) + ' N \n'
    liveForceData.text += 'Y Drag Force: ' + str(round(ballDrag.y, 3)) + ' N \n \n'

    liveForceData.text += 'X Net Force: ' + str(round(ballNetForce.x, 3)) + ' N \n'
    liveForceData.text += 'X Drag Force: ' + str(round(ballDrag.x, 3)) + ' N'

    liveMomentumData.text = 'Y Momentum: ' + str(round(ballMomentum.y, 3)) + ' N/s \n'
    liveMomentumData.text += 'X Momentum: ' + str(round(ballMomentum.x)) + ' N/s'

    # increment the time
    t += dt

# keep program running until user presses ESC key
while True:
    rate(30) # set refresh rate lower as there is no need for the program to run 100 times a second here
    exitOnKeyPress(ballScene)

