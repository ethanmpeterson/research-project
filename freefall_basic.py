# Ethan Peterson
# Basic free fall simulation where friction / air resistance is ignored
# it is assumed the ball is falling in vacuum

from visual import *
from visual.graph import *


# Modify these variables to change properties of the simulation
                 # x, y, z
gravity = vector(0, -9.8, 0) # vector objects provide some extra functionality that is useful for physics simulations. (m/s/s)
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

timeLabel = label(yoffset = 15, line = 0) # label shows the time the ball has been falling as the simulation runs
vLabel = label() # label shows the changing velocity of ball as the simulation runs
pLabel = label(yoffset = -15, line = 0) # shows changing position as the simulation runs

vILabel = label(xoffset = -110, yoffset = 15, line = 0) # shows initial velocity
vILabel.text = "Initial Velocity: " + str(ballVel.y) + " m/s"
vFLabel = label(xoffset = -110, yoffset = -15, line = 0) # shows final velocity before the ball hits the ground
vFLabel.text = "Final Velocity:" # final velocity value is added when ball hits the ground after loop finishes

pILabel = label(xoffset = 110, yoffset = 15, line = 0)
pILabel.text = "Initial Position: " + str(ballStartPos.y) + " m"
pFLabel = label(xoffset = 110, yoffset = -15, line = 0)
pFLabel.text = "Final Position:" # final position will be added after the loop finishes
# simulation loop

while ball.pos.y >= 0:
    rate(100) # set loop to run 100 times a second

    ball.pos += ballVel * dt # just in case the user defined an initial velocity at the top of file or else this will increment by 0 doing nothing

    # calulcate ball velocity
    ballVel = ballVel + gravity * dt # Same as formula: v2 = v1 + a * dt
    ball.pos += ballVel * dt # update balls position using the velocity value calculated above

    # Update vector arrows surrounding the ball
    vArrow.pos = ball.pos + (12, 0, 0) # offset position of the arrows so they do not appear inside the ball and on top of each other
    vArrow.axis = 2 * ballVel # multiply velocity by 2 to make vector arrow more visible and larger
    aArrow.pos = ball.pos + (-12, 0, 0) # ^
    aArrow.axis = gravity * 2 # multiply by 2 to make acceleration arrow more visible since it remanins constant

    # Update Graphs
    graphPos.plot(pos = (t, ball.pos.y))
    graphVel.plot(pos = (t, ballVel.y))
    graphAcc.plot(pos = (t, gravity.y))

    # update data window
    timeLabel.text = "Time: " + str(t) + " s"
    vLabel.text = "Velocity: " + str(ballVel.y) + " m/s"
    pLabel.text = "Position: " + str(ball.pos.y) + " m"

    # increment the time
    t += dt

vFLabel.text = "Final Velocity: " + str(ballVel.y) + " m/s"
pFLabel.text = "Final Position: " + str(ball.pos.y) + " m"

# keep program running until user presses ESC key
while True:
    rate(30) # set refresh rate lower as there is no need for the program to run 100 times a second here
    if ballScene.kb.keys: # wait for key event to be processed
        key = ballScene.kb.getkey() # get last key to be to be pressed
        if key == 'esc': # if the user pressed the escape key exit the program
            exit()