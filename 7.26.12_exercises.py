import turtle

wn = turtle.Screen()
wn.bgcolor("pink")
alex = turtle.Turtle()
alex.color("blue")

ship_path = [(90, 100), (-30, 100), (-120, 100), (-30, 100), (-135, ((100 * 100 + 100 * 100) ** 0.5)), (-135, 100), (-135, ((100 * 100 + 100 * 100) ** 0.5)), (135, 100)]

for (angle, distance) in ship_path:
    alex.left(angle)
    alex.forward(distance)
    


wn.mainloop()