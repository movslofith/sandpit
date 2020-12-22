import turtle

turtle.setup(400,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a housing to hold the traffic lights"""
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
# position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# a traffic light is a state machine with 3 states,
# green, amber, red. We number each state 0, 1, 2
# when the machine changes state, we change tess' position and
# fillcolor
state_num = 0

def advance_state_machine():
    global state_num 
    if state_num == 0: #transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1: # transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    else:
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

# bind the event handler to the space key
wn.onkey(advance_state_machine, "space")

wn.listen() # listen for events
wn.mainloop()