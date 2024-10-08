from turtle import Turtle,Screen
import random

is_race_on= False
screen= Screen()
user_bet=screen.textinput('Make your bet.','Which turtle will win the race? enter a color.')
screen.setup(500,400)
colors=['red','green','yellow','blue', 'pink', 'orange']
all_turtles=[]
y=-80


for color in colors:
    tim= Turtle(shape='turtle')
    tim.pu()
    tim.goto(-235,y)
    tim.color(color)
    y+=25
    all_turtles.append(tim)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        speed= random.randint(1,10)
        turtle.forward(speed)
        if(turtle.xcor()>=240):
            is_race_on=False
            if(turtle.pencolor()==user_bet):
                print(f"You win. {turtle.pencolor()} won the race.")
            else:
                print(f"You lose. {turtle.pencolor()} won the race.")
            screen.bye()
            break
            