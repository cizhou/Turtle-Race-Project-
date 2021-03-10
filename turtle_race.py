import turtle
import random
import time 

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("lavender")
turtle1.speed(5)

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("light blue")
turtle2.speed(5)

turtleref = turtle.Turtle()
turtleref.shape("turtle")
turtleref.color("black")
turtleref.speed(5)

turtleref.penup()
turtleref.goto(-275,400)
turtleref.pendown()
turtleref.goto(-275,-400)

turtleref.penup()
turtleref.goto(275,400)
turtleref.pendown()
turtleref.goto(275,-400)

turtle1.penup()
turtle2.penup()

turtle1.goto(-325,50)
turtle2.goto(-325,-50)

distance = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

turtle1.forward(random.choice(distance))

turtle.mainloop()