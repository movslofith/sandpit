import turtle

def make_window(col,ttl):
    """
    Set up the display window with background colour (col) and title (ttl).
    Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(col)
    w.title(ttl)
    return w

def make_turtle(col, psize):
    """ 
    Set up a turtle with colour (col) and pensize (psize).
    Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(col)
    t.pensize(psize)
    return t

wn = make_window("pink", "Tess and Alex dancing")
tess = make_turtle("blue", 2)
alex = make_turtle("red", 5)
dave = make_turtle("hotpink", 7)

tess.forward(100)
alex.left(90)
alex.forward(200)
dave.backward(200)

wn.mainloop()
