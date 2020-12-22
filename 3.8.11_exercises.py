def main():
    pass

if __name__ == '__main__':
    main()

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.penup()
alex.hideturtle()
alex.pensize(3)

alex.stamp()

for i in range (12):
    alex.forward(100)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(10)
    alex.stamp()
    alex.backward(120)
    alex.left(30)

