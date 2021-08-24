# import object from module turtle
from turtle import *

# initial state of spinner is null (stable)
state = {'turn': 0}

# Draw fidget spinner
def spinner():
    clear()

    # Angle of fidget spinner
    angle = state['turn']/10

    
    # To rotate in clock wise we use right
    # for Anticlockwise rotation we use left
    right(angle)

    # move the turtle forward by specified distance
    forward(100)

    # draw a dot with diameter 120 using colour blue
    dot(120, 'blue')

    # move the turtle backward by specified distance
    back(100)

    #second dot
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)

    # third dot
    right(120)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    update()


# Animate fidget spinner
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)

# Flick fidget spinner
def flick():
    #acceleration of spinner
    state['turn']+=20 

setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# wing of fidget spinner
width(20)

# keyboard key for the rotation of spinner
#click continuously to spin the spinner
onkey(flick, 'space')

listen()
animate()
done()