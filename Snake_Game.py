from turtle import Screen
import time
from Snake import Snake
from food import Food
from ScoreBoard import ScoreBoard

# Objects
score = ScoreBoard()
screen = Screen()
snake = Snake()
food = Food()

# screen customization
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


# screen control
screen.onkey(fun= snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


# movements
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_auto()


# collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_update()
        snake.plus_size()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        snake.reset()
        score.reset()

    for turtle in snake.turtles:
        if snake.head.distance(turtle) < 10 and turtle != snake.head:
            snake.reset()
            score.reset()
            # game_is_on = False

# if game_is_on == False:
#     score.game_over()

screen.exitonclick()
