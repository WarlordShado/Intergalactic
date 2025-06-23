import pygame as PyGame
from sprite import Sprite
import Globals
from consts import *

def main() -> None:
    
    PyGame.init()
    screen = PyGame.display.set_mode((WIDTH,HEIGHT))
    clock = PyGame.time.Clock()
    currentTime = 0
    prevTime = 0
    bg = Sprite("sprites/Background.png",WIDTH,HEIGHT)
    
    exit = False
    
    Globals.init(screen)

    while not exit:
        events = PyGame.event.get()
        bg.getImage(screen,(0,0))

        for event in events :
            if event.type == PyGame.QUIT:
                exit = True
            if event.type == PyGame.MOUSEBUTTONDOWN:
                if Globals.game.gameOver:
                    Globals.init(screen)
                elif not Globals.game.startGame:
                    Globals.game.startGame = True
            if event.type == PyGame.KEYDOWN:
                keys = PyGame.key.get_pressed()
                if not Globals.game.startGame:
                    if keys[PyGame.K_r]:
                        Globals.game.gearSelect()
                    
        currentTime = PyGame.time.get_ticks() #Staggers firing so it doesnt shoot every frame
        if currentTime - prevTime > Globals.game.player.gear.getFireRate():
            prevTime = currentTime
            Globals.game.changeShootState(True)

        if not Globals.game.gameOver and Globals.game.startGame:
            Globals.game.handleInput()
            Globals.game.draw()
        elif not Globals.game.startGame:
            Globals.game.StartScreen()
        else:
            Globals.game.GameOver()
       
        PyGame.display.update()
        screen.fill(Globals.BLACK)
        clock.tick(60)


if __name__ == "__main__":
    main()
