import turtle

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

turtle.color('white')
turtle.pensize(5)
turtle.hideturtle()
turtle.bgcolor('royal blue')
turtle.fillcolor('red')
turtle.begin_fill()
for x in range(8):   
    turtle.forward(100)
    turtle.left(45)
turtle.end_fill()

    
turtle.done()