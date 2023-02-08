import turtle
from random import *
from turtle import *    
snk0 = turtle.Turtle()

def forward():
    snk0.setheading(0)
    snk0.forward(10)

def left():
    snk0.setheading(270)
    snk0.forward(10)

def right():
    snk0.setheading(90)
    snk0.forward(10)

def down():
    snk0.setheading(180)
    snk0.forward(10)






# snk0.listen()
while True == True:
    bg = turtle.Screen()
    bg.setup(1000,1000)
    bg.bgcolor("black")

########## back ground map ##############


    snk0.shape("turtle")
    snk0.turtlesize(.5,.5)
    snk0.begin_fill()
    snk0.color('lime')
######### snake cusotmization ########

    # snk0.onkey(forward , 'Up')
    # snk0.onkey(left , 'Left')
    # snk0.mainloop()







