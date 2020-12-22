import turtle

turtle.setup(500,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window")
wn.bgcolor("pink")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")
tess.speed(0)

def h1(x, y):
    wn.title("Got click at coords {0}, {1}".format(x ,y))
    tess.goto(x, y)
    

wn.onclick(h1) # wire up a click on the window
wn.mainloop()
