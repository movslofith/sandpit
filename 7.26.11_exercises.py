import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
alex = turtle.Turtle()
alex.color("blue")

ship_path = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle, distance) in ship_path:
    alex.left(angle)
    alex.forward(distance)
    


wn.mainloop()