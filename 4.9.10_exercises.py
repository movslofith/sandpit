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

for i in range(5):
    draw_star(alex, 100)

    # move alex to starting position of next star 
    
    # alex.penup()
    alex.forward(350)
    alex.right(144)
    # alex.pendown()

wn.mainloop()

