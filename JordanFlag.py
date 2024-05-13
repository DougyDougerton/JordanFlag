import turtle
#Time stamp April 06, 2024 Time: 23:07

#Turtle creation 1
t = turtle.Turtle()
turtle.setup(width = 1415, height = 720)
#Speed of turtle
t.speed(3)
#Tell the turtle where to go
t.penup()
t.goto(-710, 360)
t.pendown()

#Fill the rectangle with the color of your choice
t.fillcolor("black")
#start/end the fill. 
t.begin_fill()
#Time to draw the rectangle
for i in range(2):
    t.forward(1450)
    t.right(90)
    t.forward(250)
    t.right(90)

t.end_fill()

#Turtle creation 2
t = turtle.Turtle()
turtle.setup(width = 1415, height = 720)
#Speed of turtle
t.speed(3)
#Tell the turtle where to go
t.penup()
t.goto(-710, -150)
t.pendown()

#Fill the rectangle with the color of your choice
t.fillcolor("#007a3d")
#start/end the fill. 
t.begin_fill()
#Time to draw the rectangle
for i in range(2):
    t.forward(1450)
    t.right(90)
    t.forward(225)
    t.right(90)

t.end_fill()

#Turtle creation 3
t = turtle.Turtle()
turtle.setup(width = 1415, height = 720)
#Turtle speed
t.speed(3)
#Tell the turtle where to go
t.penup()
t.goto(-705, 360)
t.pendown()
#Fill the color
t.fillcolor("#ce1126")
#Start/End fill
t.begin_fill()
for i in range(1):
    t.right(30)
    t.forward(800)
    t.right(126)
    t.forward(850)
t.end_fill()

#Turtle creation for Jordan flag star
t = turtle.Turtle()
turtle.setup(width = 1415, height = 720)
#Turtle speed
t.speed(1)
#Tell the turtle where to go
t.penup()
t.goto(-500, 20)
t.pendown()
#Fill the color
t.fillcolor("white")
#Start/End fill
t.begin_fill()
for i in range(1):
    t.left(65)
    t.forward(35) #line 1
    t.right(135)
    t.forward(35) #line 2
    t.left(90)
    t.forward(35) #line 3
    t.right(130)
    t.forward(35) #line 4
    t.left(70)
    t.forward(35) #line 5
    t.right(130)
    t.forward(35) #line 6
    t.left(85)
    t.forward(35) #line 7
    t.right(140)
    t.forward(37) #line 8
    t.left(85)
    t.forward(37) #line 9
    t.right(135)
    t.forward(35) #line 10
    t.left(85)
    t.forward(35) #line 11
    t.right(130)
    t.forward(35) #line 12
    t.left(85)
    t.forward(35) #line 13
    t.right(137)
    t.forward(37)
    
t.end_fill()

t.hideturtle()
turtle.done()
