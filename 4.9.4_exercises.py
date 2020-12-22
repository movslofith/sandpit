import turtle

def draw_four_square(t, sz):
    """
    Draw 4 sqaure grid with turtle t, of small square side length sz.
    """

    for i in range(4):

        # draw small square 4 times
        for i in range(4):
            t.forward(sz)
            t.left(90)

        t.right(90) # turn to draw next of 4 squares to make up larger square

wn = turtle.Screen()
wn.bgcolor("pink")

alex = turtle.Turtle()
alex.color("lightgreen")
alex.pensize(1)
alex.speed(0)

for i in range(6):
    draw_four_square(alex, 100)
    alex.right(360 / 20)

wn.mainloop()

