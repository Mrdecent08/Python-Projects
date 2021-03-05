import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
pen.pencolor("green")
a= 0
b= 0
pen.speed(0)
pen.penup()
pen.goto(0,200)
pen.pendown()
while True:
    pen.forward(a)
    pen.right(b)
    a += 3
    b += 1
    if b==210:
        break
    pen.hideturtle()
turtle.done()