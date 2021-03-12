import turtle
import random
import time 

races = int(input("How many races do you want?"))
turtle1score = 0 
turtle2score = 0 

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("lavender")
turtle1.speed(3)

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("light blue")
turtle2.speed(3)

turtleref = turtle.Turtle()
turtleref.shape("turtle")
turtleref.color("black")
turtleref.speed(6)

turtlefinish = turtle.Turtle()
turtlefinish.shape("turtle")
turtlefinish.color("black")
turtlefinish.speed(0)

#turtle.tracer(n=5, delay=0) 

#finish line
turtlefinish.penup()
turtlefinish.goto(250,325)
turtlefinish.pendown()
for i in range (14):
    #one row of squares
    for i in range(2):
        turtlefinish.begin_fill()
        for i in range(4):
            turtlefinish.forward(25)
            turtlefinish.left(90)
        turtlefinish.end_fill()
        turtlefinish.forward(25)
        for i in range(4):
            turtlefinish.forward(25)
            turtlefinish.left(90)
        turtlefinish.forward(25)
        #second row of squares
    turtlefinish.backward(100)
    turtlefinish.right(90)
    turtlefinish.forward(25)
    turtlefinish.left(90)
    #second row of squares
    for i in range(2):
        for i in range(4):
            turtlefinish.forward(25)
            turtlefinish.left(90)
        turtlefinish.forward(25)
        turtlefinish.begin_fill()
        for i in range(4):
            turtlefinish.forward(25)
            turtlefinish.left(90)
        turtlefinish.end_fill()
        turtlefinish.forward(25)
    turtlefinish.backward(100)
    turtlefinish.right(90)
    turtlefinish.forward(25)
    turtlefinish.left(90)

while races > 0: 
    turtleref.penup()
    turtleref.goto(-250, 300)
    turtleref.write(f"Turtle 1:{turtle1score} wins",font=("Arial", 18))
    turtleref.goto(-250, 275)
    turtleref.write(f"Turtle 2:{turtle2score} wins", font=("Arial", 18))
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
    color=["red", "orange", "yellow", "green", "blue", "purple"]

    turtle1.pendown()
    turtle2.pendown()

    while turtle1.xcor() <= turtleref.xcor() or turtle2.xcor() <= turtleref.xcor():
        turtle1.forward(random.choice(distance))
        turtle1.color(random.choice(color))
        turtle2.forward(random.choice(distance))
        turtle2.color(random.choice(color))
        continue

    if turtle1.xcor() > turtle2.xcor():
        turtle1score = turtle1score + 1
        turtle1.penup()
        turtle2.penup()
        turtleref.penup()
        turtle1.goto(0,0)
        turtle1.color("lavender")
        turtle1.write("Turtle1 Wins!", align="center", font=("Arial", 48))
    elif turtle2.xcor() > turtle1.xcor():
        turtle2score = turtle2score + 1
        turtle1.penup()
        turtle2.penup()
        turtleref.penup()
        turtle2.goto(0,0)
        turtle2.color("light blue")
        turtle2.write("Turtle2 Wins!", align="center", font=("Arial", 48))

    turtle1.goto(0,0)
    turtle2.goto(0,0)
    turtleref.goto(0,0)

    time.sleep(1)

    races = races - 1

    turtle1.clear()
    turtle2.clear()
    turtleref.clear()
    continue

turtleref.penup()
turtleref.goto(-250, 300)
turtleref.write(f"Turtle 1:{turtle1score} wins",font=("Arial", 18))
turtleref.goto(-250, 275)
turtleref.write(f"Turtle 2:{turtle2score} wins", font=("Arial", 18))

turtleref.goto(0,0)

if turtle1score > turtle2score:
    turtleref.write("Turtle 1 Won", align="center", font=("Arial", 48))
elif turtle2score > turtle1score:
    turtleref.write("Turtle 2 Won", align="center", font=("Arial", 48))
elif turtle1score == turtle2score:
    turtleref.write("Tie!", align="center", font=("Arial", 48))

turtle.mainloop()