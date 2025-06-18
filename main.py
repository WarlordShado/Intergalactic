import pygame as PyGame
from game import Game
from sprite import Sprite
from const import *

def main() -> None:
    PyGame.init()
    screen = PyGame.display.set_mode((WIDTH,HEIGHT))
    clock = PyGame.time.Clock()
    currentTime = 0
    prevTime = 0
    bg = Sprite("sprites/Background.png",WIDTH,HEIGHT)
    
    exit = False
    
    game = Game(screen,WIDTH/2,HEIGHT)

    while not exit:
        events = PyGame.event.get()
        bg.getImage(screen,(0,0))

        for event in events :
            if event.type == PyGame.QUIT:
                exit = True
            if event.type == PyGame.MOUSEBUTTONDOWN:
                if game.gameOver:
                    game = Game(screen,WIDTH/2,HEIGHT)
                elif not game.startGame:
                    game.startGame = True
            if event.type == PyGame.KEYDOWN:
                keys = PyGame.key.get_pressed()
                if not game.startGame:
                    if keys[PyGame.K_r]:
                        game.gearSelect()
                    
        currentTime = PyGame.time.get_ticks() #Staggers firing so it doesnt shoot every frame
        if currentTime - prevTime > game.player.gear.getFireRate():
            prevTime = currentTime
            game.changeShootState(True)

        if not game.gameOver and game.startGame:
            game.handleInput()
            game.draw()
        elif not game.startGame:
            game.StartScreen()
        else:
            game.GameOver()
       
        PyGame.display.update()
        screen.fill(BLACK)
        clock.tick(60)


if __name__ == "__main__":
    main()
