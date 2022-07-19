from gameturtle import PaddleGame

game = PaddleGame()
game.start()
while game.active:
    game.update()