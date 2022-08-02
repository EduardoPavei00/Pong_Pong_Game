import turtle as t



def end():
    sc = t.Screen()
    sc.clearscreen()
    sc.bgcolor("#000")
    sc.title("You Win!")
    sc.screensize(500, 800)
    firework = t.Turtle()
    firework.pensize(3)
    firework.shape("turtle")
    firework.goto(0, 0)
    firework.pendown()
    firework.stamp()
    firework.speed(100)
    firework.left(90)

    firework.color("#EA2027")
    for step in range(40):
        firework.forward(100)
        firework.left(180)
        firework.forward(100)
        firework.left(9)

    firework.color("#EE5A24")
    for step in range(36):
        firework.forward(130)
        firework.left(180)
        firework.forward(130)
        firework.left(10)

    firework.color("#F79F1F")
    for step in range(20):
        firework.forward(150)
        firework.left(180)
        firework.forward(150)
        firework.left(18)

    firework.color("#3ae374")
    for stamps in range(12):
        firework.penup()
        firework.forward(170)
        firework.pendown()
        firework.forward(10)
        firework.penup()
        firework.forward(10)
        firework.stamp()
        firework.right(30)
        firework.penup()
        firework.setpos(0, 0)

    text = t.Turtle()
    text.penup()
    text.goto(0, 400)
    text.pendown()
    text.write("You win!!", False, align="center", font=("Courier", 48, "normal"))
    text.color("#fff")
    text.penup()
    text.setpos(0, -240)
    text.write("Create by Eduardo!", True, align="center", font=("Monster", 14, "normal"))
    text.setpos(0, -280)
    text.write("Projeto no GitHub: EduardoPavei00 !!", True, align="center", font=("Monster", 12, "normal"))

    sc.mainloop()


def game_over():
    sc = t.Screen()
    sc.clearscreen()
    sc.bgcolor('#fff2b7')
    sc.title("GAME OVER!!")
    sc.screensize(500, 800)
    __pen = t.Turtle()
    __pen.pensize(10)
    __pen.fillcolor('yellow')
    __pen.hideturtle()
    radius = 180
    __pen.penup()
    __pen.setposition(0, -radius)
    __pen.setheading(0)
    __pen.pendown()
    __pen.begin_fill()
    __pen.circle(radius)
    __pen.end_fill()

    mouth_radius = radius * 0.6
    mouth_angle = 70
    __pen.penup()
    __pen.setposition(0, -20)
    __pen.setheading(180)
    __pen.pendown()
    __pen.circle(mouth_radius, mouth_angle)
    __pen.penup()
    __pen.setposition(0, -20)
    __pen.setheading(180)
    __pen.pendown()
    __pen.circle(mouth_radius, -mouth_angle)

    eye_x = 50
    eye_y = 50
    eye_size = 60
    __pen.penup()
    __pen.setposition(eye_x, eye_y)
    __pen.pendown()
    __pen.dot(eye_size)
    __pen.penup()
    __pen.setposition(-eye_x, eye_y)
    __pen.pendown()
    __pen.dot(eye_size)

    text = t.Turtle()
    text.penup()
    text.goto(0, 200)
    text.pendown()
    text.write("Game Over!!", False, align="center", font=("Courier", 48, "normal"))
    text.color("#fff")