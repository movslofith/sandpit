import turtle

def draw_poly(t, n, sz):
    """
    Draw regular polygon with turtle t, with number of sides n and of side length sz.
    """
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)

wn = turtle.Screen()
wn.bgcolor("pink")

alex = turtle.Turtle()
alex.color("lightgreen")
alex.pensize(3)

draw_poly(alex, 8, 50)

wn.mainloop()

