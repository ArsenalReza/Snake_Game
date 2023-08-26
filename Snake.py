from turtle import Turtle
import time
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_turtle()
        self.head = self.turtles[0]

    def create_turtle(self):
        for position in POSITIONS:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.shapesize(1, 1)
            turtle.goto(position)
            self.turtles.append(turtle)

    def move_auto(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(-90)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # def game_over_ani(self):
    #     for i in range(10):
    #         time.sleep(0.5)
    #         self.turtles[all].hideturtle()
    #         time.sleep(0.1)
    #         self.turtles[all].showturtle()

    def plus_size(self):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(self.turtles[-1].position())
        self.turtles.append(turtle)


    def reset(self):
        for turtle in self.turtles:
            turtle.hideturtle()
        self.turtles.clear()
        time.sleep(0.5)
        self.create_turtle()
        self.head = self.turtles[0]
