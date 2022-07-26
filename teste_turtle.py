import turtle


def fim():
    sc = turtle.Screen()
    sc.clearscreen()
    sc.bgcolor("#000")
    sc.title("You Win!")
    sc.screensize(500, 800)
    firework = turtle.Turtle()
    firework.pensize(3)
    firework.shape("turtle")
    firework.penup()
    firework.goto(0, 250)
    firework.pendown()
    firework.write("You win!!", False, align="center", font=("Courier", 48, "normal"))
    firework.penup()
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

    text = turtle.Turtle()
    text.color("#fff")
    text.penup()
    text.setpos(0, -240)
    text.write("Create by Eduardo!", True, align="center", font=("Monster", 14, "normal"))
    text.setpos(0, -260)
    text.write("Eai Erick, o 10 vem?", True, align="center", font=("Monster", 12, "normal"))
    text.setpos(0, -280)
    text.write("Projeto no GitHub: EduardoPavei00 !!", True, align="center", font=("Monster", 12, "normal"))

    sc.mainloop()
