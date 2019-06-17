import turtle
import random
import time

delay = 0.1

#set screen

wh = turtle.Screen()
wh.title("MANU GAME")
wh.bgcolor("black")
wh.setup(width=600, height=600)
wh.tracer(0)

#snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("silver")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#Score
high_score = 0
score = 0

pen.write(f"SCORE: 0 HIGH SCORE: 0", align="center", font=("Courier", 24, "normal"))


#Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "rigth":
        head.direction = "left"

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

def game_over():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    # hide segments
    for segment in segments:
        segment.goto(1000, 1000)

    # clear segments list
    segments.clear()

# Keyboard bindings
wh.listen()

wh.onkeypress(go_up, "Up")
wh.onkeypress(go_down, "Down")
wh.onkeypress(go_left, "Left")
wh.onkeypress(go_right, "Right")

# main game loop
while True:
    wh.update()

    # chack for the collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()
        # reset game
        delay = 0.1
        score = 0
        pen.clear()
        pen.write(f"SCORE: 0 HIGH SCORE: {high_score}", align="center", font=("Courier", 24, "normal"))

    # check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color('silver')
        new_segment.penup()
        segments.append(new_segment)

        # short delay
        delay -= 0.001
        # inscrease score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"SCORE: {score} HIGH SCORE: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()

        segments[0].goto(x,y)

    move()

    #check for head collision with in the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()
            # reset game
            delay = 0.1
            score = 0
            pen.clear()
            pen.write(f"SCORE: 0 HIGH SCORE: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)


wh.mainloop()