import turtle

def draw_multicolour_square(t, sz):
    """Make turtle t draw a multicolour square with sides of length sz"""
    for i in ["red", "purple", "green", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()    # setup the window and its attributes
wn.bgcolor("pink")
wn.title("Using a function to draw mutiple instances of a multicolour square")

alex = turtle.Turtle() # create turtle 'alex' and give some attributes
alex.pensize(0.5)
alex.speed(0)

size = 20 # minimum size of square

for i in range(100):
    draw_multicolour_square(alex, size) # make alex draw a multicolour square
    size = size + 1 # increase the size variable so that the next square is bigger
    alex.forward(5) # move alex forward after drawing the square
    alex.left(18)    # turn alex after drawing the square

wn.mainloop()

