import turtle

turtle.setup(400,600)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.hideturtle()
green_light = turtle.Turtle()
green_light.hideturtle()
amber_light = turtle.Turtle()
amber_light.hideturtle()
red_light = turtle.Turtle()
red_light.hideturtle()

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

# position green_light onto the place where the green light should be
green_light.penup()
green_light.forward(40)
green_light.left(90)
green_light.forward(50)
# turn green_light into a big green circle
green_light.shape("circle")
green_light.shapesize(3)
green_light.fillcolor("green")
green_light.showturtle()

# position amber_light onto the place where the amber light should be
amber_light.penup()
amber_light.forward(40)
amber_light.left(90)
amber_light.forward(120)
# turn amber_light into a big orange circle
amber_light.shape("circle")
amber_light.shapesize(3)
amber_light.fillcolor("darkorange")
amber_light.showturtle()

# position red_light onto the place where the red light should be
red_light.penup()
red_light.forward(40)
red_light.left(90)
red_light.forward(190)
# turn red_light into a big red circle
red_light.shape("circle")
red_light.shapesize(3)
red_light.fillcolor("darkred")
red_light.showturtle()


# a traffic light is a state machine with 3 states,
# green, amber, red. We number each state 0, 1, 2
# when the machine changes state, we change which turtle to show
state_num = 0

def advance_state_machine():
    """ Traffic light sequence on timer"""

    global state_num 
    if state_num == 0: #transition from state 0 to state 1
        green_light.fillcolor("green")
        amber_light.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 1: # transition from state 1 to state 2
        green_light.fillcolor("darkgreen")
        state_num = 2
        wn.ontimer(advance_state_machine, 1000)
    elif state_num == 2: # transition from state 2 to state 3
        amber_light.fillcolor("darkorange")
        red_light.fillcolor("red")
        state_num = 3
        wn.ontimer(advance_state_machine, 2000)
    else: # transition from state 3 to state 4
        red_light.fillcolor("darkred")
        green_light.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine, 3000)

# bind the event handler to the space key
wn.onkey(advance_state_machine, "space")

wn.listen() # listen for events
wn.mainloop()