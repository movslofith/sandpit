import turtle

def make_window(col, titl):
    """
    Setup up the window with the given background color (col) and title (titl).
    Returns the new window
    """
    w = turtle.Screen()
    w.bgcolor(col)
    w.title(titl)
    return w

def make_turtle(col, pensz):
    """
    Set up a new turtle of color (col) and pensize (pensz).
    Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(col)
    t.pensize(pensz)
    return t 

def draw_square(t, sz):
    """
    Draw a square using turtle t of side length sz.
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)

    # move to the new starting postion for the next square
    t.penup()
    t.forward(2 * sz)
    t.pendown()

# set up a window and a turtle

wn = make_window("lightgreen", "Drawing 5 squares")
alex = make_turtle("red", 3)

# draw 5 squares

for i in range(5):
    draw_square(alex, 20) 
    
wn.mainloop()
   