import random
import turtle as t
from turtle import TurtleScreen
from enum import Enum


# === Definições utilizadas ===


# Create Border
class ScreenBorder:
    size: float

    def __init__(self, screen: TurtleScreen):
        self.size = min(screen.window_width(), screen.window_height()) * 0.8
        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.penup()
        self.__pen.setposition(-self.size / 2, -self.size / 2)
        self.__pen.pendown()
        self.__pen.pensize(3)
        self.__pen.fillcolor('#ffe690')
        self.__pen.begin_fill()
        for side in range(4):
            self.__pen.forward(self.size)
            self.__pen.left(90)
        self.__pen.end_fill()

        self.__pen.hideturtle()


class PaddleDirection(Enum):
    NONE = 0
    RIGHT = 1
    LEFT = 2


class Paddle:
    __min_x: int
    __max_x: int
    __dx: int = 10
    width: int = 50
    height: int = 10
    __next_move = PaddleDirection.NONE

    def __init__(self, start_x, start_y, min_x, max_x):
        self.__min_x = min_x + self.width / 2
        self.__max_x = max_x - self.width / 2

        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.shape("square")
        self.__pen.fillcolor('#f2b767')
        self.__pen.shapesize(stretch_wid=self.height / 10, stretch_len=self.width / 10)
        self.__pen.penup()
        self.__pen.goto(start_x, start_y)

    def x(self):
        return self.__pen.xcor()

    def y(self):
        return self.__pen.ycor()

    def __move(self, direction: PaddleDirection):
        if direction == PaddleDirection.RIGHT:
            positions = self.__dx
        elif direction == PaddleDirection.LEFT:
            positions = -self.__dx
        else:
            return

        def undo():
            self.__pen.setx(self.__pen.xcor() - positions)

        self.__pen.setx(self.__pen.xcor() + positions)
        if self.__pen.xcor() - 20 < self.__min_x:
            print(self.__min_x)
            undo()
        if self.__pen.xcor() + 20 > self.__max_x:
            undo()

    def paddle_right(self):
        self.__next_move = PaddleDirection.RIGHT

    def paddle_left(self):
        self.__next_move = PaddleDirection.LEFT

    def update_position(self):
        self.__move(self.__next_move)
        self.__next_move = PaddleDirection.NONE


class Ball:
    """
    Ball of circle shape
    """
    radius = 8
    rotate_ball = random.choice([1, -1])

    def __init__(self, x_ini, y_ini, dx, dy):
        # TODO ball size

        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.shapesize(1)
        self.__pen.shape('circle')

        self.__pen.fillcolor('#fff4a8')
        self.__pen.penup()
        self.__pen.goto(x_ini, y_ini)

        # TODO E se eu quiser que a bola caminhasse em uma direcao diferente?
        self.dx = self.rotate_ball * dx
        self.dy = self.rotate_ball * dy

    def clear(self):
        print("teste")
        self.__pen.goto(10000, 10000)

    def x(self):
        return self.__pen.xcor()

    def y(self):
        return self.__pen.ycor()

    def update_position(self):
        self.__pen.setx(self.__pen.xcor() + self.dx)
        self.__pen.sety(self.__pen.ycor() + self.dy)

    def reset(self):
        self.dx = -1 * self.dx
        self.dy = -1 * self.dy
        return self.__pen.goto(0, -120)


class Enemy:
    __min_x: int
    __max_x: int
    width: int = 30
    height: int = 10
    color = '#d34e00'

    def __init__(self, start_x, start_y, hits):
        self.x = start_x
        self.y = start_y

        self.__pen = t.Turtle()
        self.hits = hits
        self.__pen.speed(0)
        self.__pen.shape("square")
        self.__pen.fillcolor(self.color)
        self.__pen.shapesize(stretch_wid=self.height / 10, stretch_len=self.width / 10)
        self.__pen.penup()
        self.__pen.goto(start_x, start_y)

    def x(self):
        return self.__pen.xcor()

    def y(self):
        return self.__pen.ycor()

    def hit(self):
        self.hits -= 1
        if self.hits == 0:
            self.__pen.hideturtle()
        if self.hits == 2:
            self.__pen.fillcolor('#f4a019')
        else:
            self.__pen.fillcolor('#ffea7f')
