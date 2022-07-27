# Import required library

from level_number import Level
import turtle as t
from time import sleep

from screen_win import fim


class PaddleGame:
    lives = 3
    sc = t.Screen()
    active: bool
    level = 1
    state = False

    # TODO maybe game has an end?

    def __init__(self):
        self.__pen = t.Turtle()
        self.lives = self.lives
        self.sc.title("Pong game")
        self.sc.bgcolor('#fff2b7')
        self.sc.setup(width=1000, height=600)

        self.sc.listen()
        self.sc.onkeypress(self.state_menu, "p")
        while True:
            self.sc.bgcolor('#fff2b7')
            self.__pen.penup()
            self.__pen.goto(0, 150)
            self.__pen.pendown()
            self.__pen.write("press P to start", False, align="center", font=("Courier", 48, "normal"))
            self.__pen.penup()
            self.__pen.goto(0, 100)
            self.__pen.pendown()
            self.__pen.write("try not to drop the ball:", False, align="center", font=("Courier", 35, "normal"))
            self.__pen.penup()
            self.__pen.goto(0, -50)
            self.__pen.pendown()
            self.__pen.write("How to play:", False, align="center", font=("Courier", 35, "normal"))
            self.__pen.penup()
            self.__pen.goto(0, -100)
            self.__pen.pendown()
            self.__pen.write("< and >", False, align="center", font=("Courier", 30, "normal"))
            self.__pen.hideturtle()
            if self.state is True:
                self.sc.clearscreen()
                break
        self.transition("Level :{}".format(self.level))
        position_x = [-150, -75, 0, 75, 150, -150, -75, 0, 75, 150]
        position_y = [150, 150, 150, 150, 150, 200, 200, 200, 200, 200]
        level_1 = Level(1, position_x, position_y, 4, 5)
        self.placar()
        while True:
            level_1.update()
            if len(level_1.enemies) == 0:
                self.level += 1
                print("------>", self.level)
                break
        self.transition("Level :{}".format(self.level))
        position_x = [-150, -75, 0, 75, 150, -150, -75, 0, 75, 150]
        position_y = [150, 150, 150, 150, 150, 200, 200, 200, 200, 200]
        level_2 = Level(2, position_x, position_y, 5, 6)
        self.placar()
        while True:
            level_2.update()
            if len(level_2.enemies) == 0:
                self.level += 1
                print("------>", self.level)
                break

        fim()
        sleep(3)
        self.sc.bye()

    def state_menu(self):
        print("fechou menu")
        self.state = True

    # ###
    def placar(self):
        self.__pen.penup()
        self.__pen.goto(-100, 240)
        self.__pen.pendown()
        self.__pen.write("Level:{} ".format(self.level), align="center",
                         font=("Courier", 24, "normal"))

    def transition(self, frase):
        self.sc.clearscreen()
        self.sc.bgcolor('#fff2b7')
        self.__pen.speed(0)
        self.__pen.penup()
        self.__pen.goto(0, 0)
        self.__pen.pendown()
        self.__pen.write(frase, False, align="center", font=("Courier", 48, "normal"))
        self.__pen.hideturtle()
        sleep(2)


    def clear(self):
        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.shape("square")
        self.__pen.color("black")
        self.__pen.shapesize(stretch_wid=1000, stretch_len=1000)

        # self.sc.update()

    def start(self):
        self.active = True
