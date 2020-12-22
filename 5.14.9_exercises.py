import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("black", "gray")

def draw_bar(t, height):
    """ Get turtle t to draw a bar, of height"""
    if height >= 200:
        t.color("black", "red")
    elif 100 <= height < 200:
        t.color("black", "yellow")
    else:
        t.color("black", "green")

    t.begin_fill()
    t.left(90)
    t.forward(height) # draw the left side of the bar
    
    t.penup()
    if height < 0:
        t.forward(-15)
    
    t.write(' ' + str(height))

    if height < 0:
        t.forward(15)
    t.pendown()
    
    t.right(90)
    t.forward(40) # draw the width of the bar
    t.right(90)
    t.forward(height) # draw the right side of the bar
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10) # leave a gap to the next bar
    t.pendown()
    
xs = [48, -65, 117, -200, 240, -160, 260, 220]

for v in xs:
    draw_bar(alex, v)
