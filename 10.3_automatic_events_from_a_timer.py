import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer to get events!")
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(2)

def h1():
    alex.forward(100)
    alex.left(56)
    wn.ontimer(h1, 60)

h1()
wn.mainloop()

