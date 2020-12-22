def main():
    pass

if __name__ == '__main__':
    main()

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

points = int(input("How many points d'ya want on this 'ere star? "))

angle = 720 / points
init_heading = (180 - (1.5 * (180 - angle)) - 90)

alex.left(init_heading)

for i in range(points):
    alex.forward(100)
    alex.left(angle)

