#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      me1was
#
# Created:     12/08/2020
# Copyright:   (c) me1was 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import turtle
import math

wn = turtle.Screen()
alex = turtle.Turtle()

heading = 0                                             # initial heading is zero degrees
turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]   # list of headings taken

for i in turns:
    alex.left(i)
    alex.forward(100)
    heading = heading + i

heading = heading % 360
print("Final drunk pirate heading is:", heading)

