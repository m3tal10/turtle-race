from turtle import Turtle,Screen
tim=Turtle()
screen= Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.back(10)
def rotate_clockwise():
    tim.setheading((tim.heading()-5))
def rotate_anticlockwise():
    tim.setheading((tim.heading()+5)%360)
def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(move_forward,'w')
screen.onkey(move_backward,'s')
screen.onkey(rotate_clockwise,'d')
screen.onkey(rotate_anticlockwise,'a')
screen.onkey(clear, 'c')

screen.exitonclick()