import turtle

def draw_spiral(t, side_length, side_growth, turns, turn_angle):
    """
    Draw a straight-sided spiral using turtle t with initial side_length, side_growth, number of turns and turn_angle.
    """
    for i in range(turns):
        t.forward(side_length)
        t.right(turn_angle)
        side_length = side_length + side_growth
      
wn = turtle.Screen()
wn.bgcolor("pink")

alex = turtle.Turtle()
alex.color("lightgreen")
alex.pensize(1)
alex.speed(0)

draw_spiral(alex, 3, 3, 100, 89)
   

wn.mainloop()

