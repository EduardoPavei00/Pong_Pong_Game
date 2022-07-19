# Import required library
from models import Paddle, ScreenBorder, Ball, PaddleDirection, Enemies
import turtle as t


class PaddleGame():
#
    sc = t.Screen()
    active: bool
    # TODO maybe game has an end?
    lives = 3

    def __init__(self):
        self.sc.title("Pong game")
        self.sc.bgcolor("white")
        self.sc.setup(width=1000, height=600)

        # Create Border
        self.border = ScreenBorder(self.sc)

        # Create Paddle
        self.paddle = Paddle(0, -200, -self.border.size / 2, self.border.size / 2)
        # self.enemies = Enemies(100,100)

        # Create Ball
        self.ball = Ball(0, 0, +3, +4)

        # Keyboard bindings
        self.sc.listen()
        self.sc.onkeypress(self.paddle.paddle_right, "Right")
        self.sc.onkeypress(self.paddle.paddle_left, "Left")

    #create_enemies:

        self.position_x = [-100, -50, 50, 100]
        self.position_y = [100, 100, 150, 150]
        for i in range(len(self.position_x)):
            self.enemies = Enemies(self.position_x[i],self.position_y[i])

    def detect_ball_in_border(self):
        if self.ball.x() > (self.border.size / 2) or self.ball.x() < (-self.border.size / 2):
            self.ball.dx *= -1

        if self.ball.y() > (self.border.size / 2):
            self.ball.dy *= -1
        elif self.ball.y() < -(self.border.size / 2):
            self.ball.reset()
            self.ball.dy *= -1
            self.lives -= 1

    def detect_ball_in_paddle(self):
        pad_x_min = self.paddle.x() - (self.paddle.width / 2)
        pad_x_max = self.paddle.x() + (self.paddle.width / 2)
        pad_y = self.paddle.y() + self.paddle.height
        ball_x = self.ball.x()
        ball_y = self.ball.y()  # + ? (raio, diametro, zero)...

        if pad_x_min <= ball_x <= pad_x_max and ball_y <= pad_y:
            self.ball.dy *= -1

    def detect_enemies_in_paddle(self):
        ball_x = self.ball.x()
        ball_y = self.ball.y()
        enemies_x_min = self.enemies.x() - (self.enemies.width/2)
        enemies_x_max = self.enemies.x() + (self.enemies.width / 2)
        enemies_y_min = self.enemies.y() - (self.enemies.height/2)
        enemies_y_max = self.enemies.y() + (self.enemies.height/2)

        if enemies_y_min <= ball_y <= enemies_y_max or enemies_x_min <= ball_x <= enemies_x_max:
            self.ball.dy *= -1

    def update(self):
        self.sc.update()
        self.ball.move()
        self.detect_ball_in_border()
        self.detect_ball_in_paddle()
        self.detect_enemies_in_paddle()


    def start(self):
        self.active = True