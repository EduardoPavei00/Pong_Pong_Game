# Import required library
from models import Paddle, ScreenBorder, Ball, PaddleDirection, Enemy, Enemy
import turtle as t
import tkinter as Canvas


def create_enemies(x_positions, y_positions):
    enemies = []
    for i in range(len(x_positions)):
        x = Enemy(x_positions[i], y_positions[i])
        enemies.append(x)
    return enemies


class PaddleGame:
    sc = t.Screen()
    active: bool
    # TODO maybe game has an end?

    def __init__(self):
        self.lives = 3
        self.sc.title("Pong game")
        self.sc.bgcolor("white")
        self.sc.setup(width=1000, height=600)


        # Create Border
        self.border = ScreenBorder(self.sc)
        self.draw()

        # Create Paddle
        self.paddle = Paddle(0, -200, -self.border.size / 2, self.border.size / 2)
        # self.enemies = Enemies(100,100)

        self.position_x = [-150, -75, 0, 75, 150, -150, -75, 0, 75, 150]
        self.position_y = [150, 150, 150, 150, 150, 200, 200, 200, 200, 200]
        self.enemies = create_enemies(self.position_x, self.position_y)

        # Create Ball
        self.ball = Ball(0, 0, +3, +4, )

        # Keyboard bindings
        self.sc.listen()
        self.sc.onkeypress(self.paddle.paddle_right, "Right")
        self.sc.onkeypress(self.paddle.paddle_left, "Left")

    def draw(self):
        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.penup()
        self.__pen.goto(0, 240)
        self.__pen.pendown()
        self.__pen.write("Lives : {} ".format(self.lives), align="center", font=("Courier", 24, "normal"))
        self.__pen.hideturtle()

    def detect_ball_in_border(self):
        ball_x_min = self.ball.x() - self.ball.radius * 10
        ball_x_max = self.ball.x() + self.ball.radius * 10
        ball_y_min = self.ball.y() - self.ball.radius * 10
        ball_y_max = self.ball.y() + self.ball.radius * 10

        if ball_x_max > (self.border.size / 2) or ball_x_min < (-self.border.size / 2):
            self.ball.dx *= -1

        if ball_y_max > (self.border.size / 2):
            self.ball.dy *= -1
        elif ball_y_min < -(self.border.size / 2):
            self.lives -= 1
            self.__pen.clear()
            self.__pen.write("Lives : {} ".format(self.lives), align="center", font=("Courier", 24, "normal"))
            self.ball.reset()

    def detect_ball_in_paddle(self):
        pad_x_min = self.paddle.x() - (self.paddle.width / 2)
        pad_x_max = self.paddle.x() + (self.paddle.width / 2)
        pad_y = self.paddle.y() + self.paddle.height
        ball_x = self.ball.x() + self.ball.radius * 10
        ball_y = self.ball.y() - self.ball.radius * 10

        if pad_x_min <= ball_x <= pad_x_max and ball_y <= pad_y:
            self.ball.dy *= -1

    def detect_enemies(self):
        ball_x_min = self.ball.x() - self.ball.radius * 10
        ball_x_max = self.ball.x() + self.ball.radius * 10
        ball_y_min = self.ball.y() - self.ball.radius * 10
        ball_y_max = self.ball.y() + self.ball.radius * 1

        for e in self.enemies:
            enemies_x_min = e.x - (e.width / 2)
            enemies_x_max = e.x + (e.width / 2)
            enemies_y_min = e.y - (e.height / 2)
            enemies_y_max = e.y + (e.height / 2)
            if ball_y_max <= enemies_y_min and (enemies_x_min <= ball_x_min <= enemies_x_max or enemies_x_min <= ball_x_max <= enemies_x_max):
                self.ball.dy *= -1

            elif ball_y_min >= enemies_y_max and (enemies_x_min <= ball_x_min <= enemies_x_max or enemies_x_min <= ball_x_max <= enemies_x_max):
                self.ball.dy *= -1

    def update(self):
        self.detect_enemies()
        self.detect_ball_in_border()
        self.detect_ball_in_paddle()
        self.ball.move()
        self.sc.update()

    def start(self):
        self.active = True
