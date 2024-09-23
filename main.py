import turtle
from random import randint
import threading

ws = turtle.Screen()
ws.bgcolor("light blue")

turtle_draw = turtle.Turtle()
score_draw = turtle.Turtle()
quit_timer = threading.Timer(2.0,quit)
score = 0

def turtle_icon_draw(x,y):
    turtle_draw.shape("turtle")
    turtle_draw.color("green")
    turtle_draw.penup()
    turtle_draw.goto(x,y)
    turtle_draw.forward(0)
    turtle_draw.turtlesize(stretch_wid=2, stretch_len=3, outline=5)
    turtle_draw.pendown()

def score_plus(x,y):
    global score
    score += 1
    score_draw.clear()

def score_board():
    score_draw.penup()
    score_draw.goto(0,300)
    score_draw.hideturtle()
    score_draw.pendown()
    score_draw.write(f"Score : {score}",align="center",font=("Arial",24,"bold"))
    if score == 10:
        score_draw.clear()
        score_draw.write("You win!!", align="center", font=("Arial", 24, "bold"))
        quit_timer.start()

while True:
    rand_x = randint(-300,300)
    rand_y = randint(-300,300)
    score_board()
    turtle_draw.onclick(score_plus)
    for i in range(2):
        turtle_icon_draw(rand_x,rand_y)
    turtle_draw.clear()