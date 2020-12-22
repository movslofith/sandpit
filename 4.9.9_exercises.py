import turtle

def draw_star(t, sz):
    """ 
    Draw 5 pointed star using turtle t of side length sz.
    """
    for i in range(5):
        t.forward(sz)
        t.right(144)

wn = turtle.Screen()
alex = turtle.Turtle()

draw_star(alex, 100)

wn.mainloop()

