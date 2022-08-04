import turtle
import random
die = [1, 2, 3, 4, 5, 6]
steps = random.choice(die)
screen = turtle.getscreen()

dexter = turtle.Turtle()
dexter.circle(15)
dexter.fillcolor("red")
dexter.rt(90)
dexter.penup()
dexter.fd(50)
dexter.pendown()

dexter_2 = dexter.clone()
dexter_2.fillcolor("blue")
dexter_2.circle(15)
dexter_2.rt(90)
screen.exitonclick()


