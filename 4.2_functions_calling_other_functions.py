import turtle
__import__("turtle").__traceable__ = False

def draw_rectangle(t, w ,h):
    """Get turtle t to draw a rectangle of width w and height h"""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


def draw_square(tx, sz):
    """Make turtle t draw a square with sides of length sz"""
    draw_rectangle(tx, sz, sz)

wn = turtle.Screen()    # setup the window and its attributes
wn.bgcolor("pink")
wn.title("Using a function to draw a square")

alex = turtle.Turtle()
draw_square(alex, 50)

draw_rectangle(alex, 50, 100)

wn.mainloop()

