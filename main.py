import random
from turtle import Turtle,Screen
colors=["red","yellow","green","blue","orange","purple"]
screen=Screen()
screen.setup(width=1080,height=720)
yPosition=-300
all_turtles=[]
user_bet=screen.textinput(title="Make your bet",prompt="Enter winning turtle's Color:")
for col in colors:
    t=Turtle(shape="turtle")
    t.color(col)
    t.penup()
    t.goto(x=-500,y=yPosition)
    yPosition+=100
    all_turtles.append(t)
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>500:
            is_race_on=False
            win_color=turtle.pencolor()
            if win_color == user_bet:
                print(f"You win ! Win color: {win_color}")
            else:
                print(f"You have Lost ! Win color: {win_color}")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)




#print(user_bet)
screen.exitonclick()