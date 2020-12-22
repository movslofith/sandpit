import turtle

turtle.setup(400,500)           # Determine the window size
wn = turtle.Screen()            # Get a reference to the window
wn.title("Handling keypresses") # Change the window title
wn.bgcolor("pink")              # Change the background colour
tess = turtle.Turtle()          # Create turtle called tess

# The next four functions are 'event handlers'

def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()                    # Close down the turtle window

def h5():
    tess.backward(30)

def h6():
    tess.color("red")

def h7():
    tess.color("green")

def h8():
    tess.color("blue")

tess_pen = 1

def pensize_up():
    global tess_pen
    if tess_pen <= 20:
        tess_pen += 1
        tess.pensize(tess_pen)

def pensize_down():
    global tess_pen
    if tess_pen >= 1:
        tess_pen -= 1
        tess.pensize(tess_pen)

shape_num = 0
def tess_shape():
    global shape_num
    shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"] 
    shape_num += 1
    shape_num % 5
    tess.shape(shapes[shape_num])

# These lines 'wire up' keypresses to the handlers we've defined

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "Down")
wn.onkey(h6, "r")
wn.onkey(h7, "g")
wn.onkey(h8, "b")
wn.onkey(pensize_up, "+")
wn.onkey(pensize_down, "-")
wn.onkey(tess_shape, "s")


# Now we tell the window to start listening for events, f
# if any of the keys we're monitoring are pressed, its
# handler will be called

wn.listen()
wn.mainloop()