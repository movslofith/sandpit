def main():
    pass

if __name__ == '__main__':
    main()

import turtle

wn = turtle.Screen()

background_color = input("What colour would you like the background to be? ")
alex_color = input("What colour would you like alex the turtle to be? ")
tess_color = input("What colour would you like tess the turtle to be? ")
line_thickness = int(input("What thickness of line would you like? "))

# wn = turtle.Screen()
wn.bgcolor(background_color)
wn.title("Hello")

alex = turtle.Turtle()
tess = turtle.Turtle()
alex.color(alex_color)
tess.color(tess_color)
alex.pensize(line_thickness)
tess.pensize(line_thickness)

# make alex draw a square
for i in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)


# make tess draw a triangle
for i in range(3):
    tess.forward(80)
    tess.left(120)

wn.mainloop()




