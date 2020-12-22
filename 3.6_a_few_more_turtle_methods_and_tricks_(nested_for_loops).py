def main():
    pass

if __name__ == '__main__':
    main()

import turtle
wn = turtle.Screen()
wn.bgcolor("pink")
alex = turtle.Turtle()
alex.shape("circle")        # make alex's shape a circle (arrow,blank,classic,square,triangle,turtle) are avaiable
alex.color("yellow")
alex.speed(0)

shps = ["arrow","classic","square","triangle","turtle"]

alex.penup()                    # lift the pen off the canvas
size = 10                       # declare variable "size"
for i in range(50):             # start for loop with 50 iterations
    for j in shps:
        alex.shape(j)
        alex.stamp()            # stamp impression of alex's shape on the canvas
        size = size + 1         # increase the size of "size" variable
        alex.forward(size)      # move alex forward by distance "size"
        alex.right(24)          # turn alex by 24 degrees to the right


wn.mainloop()