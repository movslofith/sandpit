import turtle

def draw_poly(t, n, sz):
    """
    Draw regular polygon with turtle t, with number of sides n and of side length sz.
    """
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)

def draw_equitriangle (t, sz):
    draw_poly(t, 3, sz)

wn = turtle.Screen()
wn.bgcolor("pink")

alex = turtle.Turtle()
alex.color("lightgreen")
alex.pensize(3)

draw_equitriangle(alex, 100)


wn.mainloop()

