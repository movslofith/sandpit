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

# These lines 'wire up' keypresses to the handlers we've defined

wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "Down")

# Now we tell the window to start listening for events, f
# if any of the keys we're monitoring are pressed, its
# handler will be called

wn.listen()
wn.mainloop()