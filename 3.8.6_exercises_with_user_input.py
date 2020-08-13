# program to draw shape of user determined number of sides and side length centred about the centre of the display window


def main():
    pass

if __name__ == '__main__':
    main()

import turtle
import math

wn = turtle.Screen()
alex = turtle.Turtle()

sides = int(input("How many sides would you like the shape to have? "))
side_length = int(input("How long would you like each of the sides to be? "))

ang = ((180 - (360 / sides)) / 360 ) * math.pi  # ang is the internal angle of the shape vertex
ang = ang % (math.pi / 2)                       # modulus prevents negative math.tan value resulting in negative y_offset

y_offset = (side_length / 2) * math.tan(ang)    # y_offset gives the distance alex must move vertically to the start position

# move turtle (alex) to starting position which means shape is drawn in centre of window

alex.penup()
alex.right(90)
alex.forward(y_offset)
alex.left(90)
alex.pendown()

# draw shape

alex.forward(side_length / 2)
alex.left(360 / sides)

for i in range(sides - 1):
    alex.forward(side_length)
    alex.left(360 / sides)

alex.forward(side_length / 2)

print("All done!")

