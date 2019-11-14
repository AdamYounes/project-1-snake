
# Inspired by Christian Thompsons snake.

import turtle
import time
import random
delay = 0.1

# score
score = 0
high_score = 0

# background
screen = turtle.Screen()
screen.title("Snake in Creek")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# character :)
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal" ))

# def keypresses

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# def movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keybinding
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
   
# Loop
while True:
    screen.update()

    # The mortal way...
    if head.xcor()>280 or head.xcor()<-280 or head.ycor()>280 or head.ycor()<-280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide tail when ded
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()

        # reset(score)
        score = 0

        delay = 0.1

        pen.clear()
        pen.write("score: {}  High Score {}".format(score, high_score), align="center", font=("Arial", 24, "normal" ))

    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)
        
        # tail
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # decrease the delay
        delay -= 0.001

        # score increase
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("score: {}  High Score {}".format(score, high_score), align="center", font=("Arial", 24, "normal" ))

    # tail .2
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # attach the tail :)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # way to become immortal .2
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide tail when ded
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            # reset(score)
            score = 0

            delay = 0.1

            pen.clear()
            pen.write("score: {}  High Score {}".format(score, high_score), align="center", font=("Arial", 24, "normal" ))
    
    time.sleep(delay)

screen.mainloop()