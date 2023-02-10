import turtle
from random import *
from turtle import *    

snk0 =Turtle()

def forward():
    snk0.setheading(90)
    snk0.forward(10)
    direction = "up"
    if direction != "down":
        bg.onkey(up , 'Up')

def left():
    snk0.setheading(180)
    snk0.forward(10)
    direction = "left"
    if direction != "right":
        bg.onkey(left , 'Left')
def right():
    snk0.setheading(0)
    snk0.forward(10)
    direction = "right"
    if direction != "left":
        bg.onkey(right , 'Right')


def Down():
    snk0.setheading(270)
    snk0.forward(10)
    direction = "down"
    if direction != "up":
        bg.onkey(Down , 'Down')
   



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




    
    bg.onkey(down , 'Down')
    turtle.listen()
    turtle.mainloop()










