import turtle as t

import gameturtle
from models import ScreenBorder, Paddle, Ball, Enemy
from screen_draw import end, game_over


def create_enemies(x_positions, y_positions, hits):
    enemies = []
    for i in range(len(x_positions)):
        x = Enemy(x_positions[i], y_positions[i], hits)
        enemies.append(x)
    return enemies


class Level:
    sc = t.Screen()
    active: bool
    level = 1
    state = False

    def __init__(self, hits, list_position_x, list_position_y, velocity_ball_x, velocity_ball_y):
        self.sc.clearscreen()
        self.__pen = t.Turtle()
        self.sc.bgcolor('#fff2b7')

        self.sc.clearscreen()
        self.border = ScreenBorder(self.sc)
        self.sc.bgcolor('#fff2b7')
        self.draw()
        # Create Paddle
        self.paddle = Paddle(0, -200, -self.border.size / 2, self.border.size / 2)
        # self.enemies = Enemies(100,100)

        # self.position_x = [-150, -75, 0, 75, 150, -150, -75, 0, 75, 150, -150, -75, 0, 75, 150]
        # self.position_y = [150, 150, 150, 150, 150, 200, 200, 200, 200, 200, 100, 100, 100, 100, 100]
        self.enemies = create_enemies(list_position_x, list_position_y, hits)

        self.ball = Ball(0, 0, velocity_ball_x, velocity_ball_y)


        self.sc.listen()
        self.sc.onkeypress(self.paddle.paddle_right, "Right")
        self.sc.onkeypress(self.paddle.paddle_left, "Left")
        self.sc.onkeypress(self.paddle.paddle_right, "d")
        self.sc.onkeypress(self.paddle.paddle_left, "a")

    def draw(self):
        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.penup()
        self.__pen.goto(100, 240)
        self.__pen.pendown()
        self.__pen.write("  Lives:{} ".format(gameturtle.PaddleGame.lives), align="center",
                         font=("Courier", 24, "normal"))
        self.__pen.hideturtle()

    def detect_ball_in_border(self):
        ball_x_min = self.ball.x() - self.ball.radius
        ball_x_max = self.ball.x() + self.ball.radius
        ball_y_min = self.ball.y() - self.ball.radius
        ball_y_max = self.ball.y() + self.ball.radius

        if ball_x_max > (self.border.size / 2) or ball_x_min < (-self.border.size / 2):
            self.ball.dx *= -1

        if ball_y_max > (self.border.size / 2):
            self.ball.dy *= -1
        elif ball_y_min < -(self.border.size / 2):
            gameturtle.PaddleGame.lives -= 1
            self.__pen.clear()
            self.draw()
            self.ball.reset()
            if gameturtle.PaddleGame.lives <= 0:
                game_over()

    def detect_ball_in_paddle(self):

        ball_x_min = self.ball.x() - self.ball.radius
        ball_x_max = self.ball.x() + self.ball.radius
        ball_y_min = self.ball.y() - self.ball.radius
        ball_y_max = self.ball.y() + self.ball.radius

        pad_x_min = self.paddle.x() - self.paddle.width
        pad_x_max = self.paddle.x() + self.paddle.width
        pad_y_max = self.paddle.y() + self.paddle.height
        pad_y_min = self.paddle.y() - self.paddle.height

        if ball_x_max + self.ball.dx > pad_x_min and ball_x_min + self.ball.dx < pad_x_max \
                and ball_y_max > pad_y_min and ball_y_min < pad_y_max:
            self.ball.dx *= -1
        if ball_x_max > pad_x_min and ball_x_min < pad_x_max and ball_y_max + self.ball.dy > pad_y_min \
                and ball_y_min + self.ball.dy < pad_y_max:
            self.ball.dy *= -1

    def detect_enemies(self):
        ball_x_min = self.ball.x() - self.ball.radius
        ball_x_max = self.ball.x() + self.ball.radius
        ball_y_min = self.ball.y() - self.ball.radius
        ball_y_max = self.ball.y() + self.ball.radius

        for e in self.enemies:
            enemies_x_min = e.x - e.width
            enemies_x_max = e.x + e.width
            enemies_y_min = e.y - e.height
            enemies_y_max = e.y + e.height

            if ball_x_max + self.ball.dx > enemies_x_min and ball_x_min + self.ball.dx < enemies_x_max \
                    and ball_y_max > enemies_y_min and ball_y_min < enemies_y_max:
                self.ball.dx *= -1

                if e.hits != 1:
                    print(e.hits)
                    e.hit()
                else:
                    print('remove')
                    self.enemies.remove(e)
                    e.hit()
                    if len(self.enemies) == 0:
                        self.level += 1

            if ball_x_max > enemies_x_min and ball_x_min < enemies_x_max and ball_y_max + self.ball.dy > enemies_y_min \
                    and ball_y_min + self.ball.dy < enemies_y_max:
                self.ball.dy *= -1
                if e.hits != 1:
                    print(e.hits)
                    e.hit()
                else:
                    print('remove')
                    self.enemies.remove(e)
                    e.hit()
                if len(self.enemies) == 0:
                    self.level += 1

    def clear(self):
        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.shape("square")
        self.__pen.color("black")
        self.__pen.shapesize(stretch_wid=1000, stretch_len=1000)

    def update(self):

        self.detect_enemies()
        self.detect_ball_in_border()
        self.detect_ball_in_paddle()
        self.ball.update_position()
        self.paddle.update_position()

        # self.sc.update()

    def start(self):
        self.active = True
